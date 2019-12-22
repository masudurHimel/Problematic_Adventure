.model small
.stack 100h


.data 

        fibResult dw ? ;for storing the result which is the 23rd fib number indexing starting from 1
        
.code


main proc
    
        mov ax,@data
        mov ds,ax 
        
        
        mov ax,1 ;for counting generated fib numbers
        
       
        push 1d     ;pushing first fib number
        push 1d     ;pushing second fib number                            
        mov si,3
        
        fibGenerator:
            pop bx  ;popping the last fib number after each iteration
            pop ax  ;popping the second last fib number after each iteration
            add ax,bx
            push bx         ; each time pushing the last two fib number for further use
            push ax         
            inc si
            cmp si,24      ;as we are interested in 23rd fib number
            jz end
            jmp fibGenerator
            
            
        end:
            pop ax               ;popping the result
            mov fibResult[0],ax  ;storing the result in this variable
        
            hlt     
                
        
                     
       
        
        
    
    
    
endp main
end main