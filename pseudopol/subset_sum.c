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


//finds the maximal possible sum <=max
size_t find_max(size_t N, const unsigned int *objects, size_t max_value){ 
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
