.model small
.stack 100h


.data 

        fibResult dw ? 
        
.code


main proc
    
        mov ax,7500h
        mov ds,ax 
        
        
        mov ax,1 ;for counting generated fib numbers
        
       
        push 1d     ;pushing first fib number
        push 1d     ;pushing second fib number                            
        mov si,3
        
        mov di,0h  
        
        mov word ptr ds:[di],1
        inc di
        mov word ptr ds:[di],1
        
        
        fibGenerator:
            
            inc di
            
            pop bx  ;popping the last fib number after each iteration
            pop ax  ;popping the second last fib number after each iteration
            add ax,bx
            push bx         ; each time pushing the last two fib number for further use
            push ax         
            inc si
            cmp si,51      ;as we are interested in 23rd fib number
            jz end 
            
            mov word ptr ds:[di],ax
            jmp fibGenerator
            
            
        end:
            hlt     
                
        
                     
       
        
        
    
    
    
endp main
end main