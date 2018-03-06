#include <stdlib.h>
#include <stdio.h>

typedef unsigned long long int BitField;

const size_t BITS_IN_BYTES=8;
const size_t MASK_SIZE_IN_BYTES=sizeof(BitField);
const size_t MASK_SIZE=8*sizeof(BitField);
const BitField ZERO=0;
const BitField ONE=1;


//not the fastest, but portable
unsigned int first_set_bit(BitField mask){
    unsigned int res=MASK_SIZE;
    BitField start=ONE<<(MASK_SIZE-1);
    while(start>0){
        if((start&mask)!=0)
            return res;
         res--;
         start>>=1;
    }
    return 0;  
}

BitField *get_reachable(size_t N, const unsigned int *objects, size_t max_value){
   size_t size=(max_value+MASK_SIZE)/MASK_SIZE;
   BitField *reachable=(BitField*)calloc(size, MASK_SIZE);

   //printf("size %zu\n", size); 
   //only 0 is reachable at start/without objects:
   reachable[0]=1UL;

   //processing a whole mask in parallel:
   for(size_t id=0;id<N;id++){
      size_t global_offset=objects[id]/MASK_SIZE;
      size_t shift_lower=objects[id]%MASK_SIZE;
      size_t shift_higher=MASK_SIZE-shift_lower;
      //printf("offset %zu, shift_lower %zu, shift_higher %zu\n", global_offset, shift_lower, shift_higher);
      for(size_t current=size-1;current<size;current--){
           //printf("current: %zu, value=%llu\n", current, reachable[current]);
           BitField lower_stamp=reachable[current]<<shift_lower;
           //shifting by more/equal than MASK_SIZE is undefined behaviour:
           BitField higher_stamp=shift_lower==0 ? 0 :reachable[current]>>shift_higher;
           //printf("lower_stamp %llu, higher_stamp %llu\n", lower_stamp, higher_stamp);
           if(current+global_offset<size){
                 reachable[current+global_offset]|=lower_stamp;
                 if(current+global_offset+1<size){
                      reachable[current+global_offset+1]|=higher_stamp;
                 }
           }
      }
   }
   //null all bits > max_values:
   BitField mask=(ONE<<((max_value+1)%MASK_SIZE))-1;
   if(mask!=0){//mask 0 means all bits needed
        reachable[size-1]&=mask;
   }

   return reachable;
}


//finds the maximal possible sum <=max
size_t find_max(size_t N, const unsigned int *objects, size_t max_value){ 

   BitField *reachable=get_reachable(N, objects, max_value);
   size_t size=(max_value+MASK_SIZE)/MASK_SIZE;

   //stop with the highest bit
   size_t res=0;
   for(size_t current=size-1;current<size;current--){
      if(reachable[current]!=0){
          res=current*MASK_SIZE+first_set_bit(reachable[current])-1;
          break;
      }
   }

   free(reachable);
   return res;
}


//true if there is a non-empty subset with sum=0, false otherwise
int find_if_subset_sum_exists(size_t n_pos, unsigned int *positives, size_t n_neg, unsigned int *negatives){
    size_t max_value=0;
    for(size_t i=0;i<n_pos;i++){
      max_value+=positives[i];
    }

    //stamp positive objects:
    BitField *reachable=get_reachable(n_pos, positives, max_value);
    size_t size=(max_value+MASK_SIZE)/MASK_SIZE;

    //stamp negative objects:
   
    //processing a whole mask in parallel:
    int found=0;
    for(size_t id=0;id<n_neg && !found;id++){
        size_t global_offset=negatives[id]/MASK_SIZE;
        size_t shift_lower=negatives[id]%MASK_SIZE;
        size_t shift_higher=MASK_SIZE-shift_lower;
        //printf("offset %zu, shift_lower %zu, shift_higher %zu\n", global_offset, shift_lower, shift_higher);
        for(size_t current=0;current<size;current++){
           //printf("current: %zu, value=%llu\n", current, reachable[current]);
           BitField lower_stamp=shift_lower==0 ? 0 :reachable[current]>>shift_higher;
           //shifting by more/equal than MASK_SIZE is undefined behaviour:
           BitField higher_stamp=reachable[current]<<shift_lower;

           size_t index=current-global_offset;
           if(index<size){
                 if(index==0 && (1&higher_stamp)==1){//0 reached
                      found=1;
                      break;
                 }
                 reachable[index]|=higher_stamp;
                 index--;
                 if(index<size){
                     //if(index==0 && (1&lower_stamp)==1){//0 reached, but not needed for lower, because 1 bit is always 0
                     reachable[index]|=lower_stamp;
                 }
           }
        }
    }

    free(reachable);
    return found; 
}


//1if there is a non-empty subset with sum=0, 0 otherwise
int subset_sum_exists(size_t N, const int *objects){
    int found=0;
    size_t n_pos=0;
    unsigned int *positives=(unsigned int*)calloc(N, sizeof(unsigned int));

    size_t n_neg=0;
    unsigned int *negatives=(unsigned int*)calloc(N, sizeof(unsigned int));

    for(size_t i=0;i<N;i++){
        if(objects[i]==0){
            found=1;
            break;
        }
        else if(objects[i]>0){
             positives[n_pos++]=objects[i];   
        }
        else{
             //because of undefined behavior of -MIN_INT
             int n = objects[i];
             negatives[n_neg++]= n<0 ? -((unsigned int)n) : (unsigned int) n;
        }
    }

    if(!found){
        found = find_if_subset_sum_exists(n_pos, positives, n_neg, negatives);
    }

    free(positives);
    free(negatives);
    return found;
}


