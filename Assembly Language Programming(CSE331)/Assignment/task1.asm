include "emu8086.inc"
.model small
.stack 100h

 
 
.data

    posString db "Positive$"
    negString db "Negative$"

.code 

newLine macro 
    
        mov ah,02
        mov dl,10
        int 21h
        
        mov ah,02
        mov dl,13
        int 21h 
        
endm newLine        


main proc
    
     mov ax,@data
     mov ds,ax
    
     CALL SCAN_NUM          ;used this procedure to store data in CL as it is mentioned in question
     DEFINE_SCAN_NUM
     
     
     mov si,0
     
     cmp cl,0               ;comparing with 0 , so if negative the resulted value will be less than 0 and vice versa
     
     newLine                ;macro for putting new line
     
     jl negative
     
     jmp positive
     
     
     negative:                    ;section for printing negative
      
           mov ah,02
           mov dl,negString[si] 
           cmp dl,'$'
           jz end
           int 21h 
           inc si
           jmp negative   
                                  ;section for printing positive
     positive:
     
           mov ah,02
           mov dl,posString[si] 
           cmp dl,'$'
           jz end
           int 21h 
           inc si
           jmp positive
              
              
              
     end:
        
        hlt          
     
    
    
endp main
end main