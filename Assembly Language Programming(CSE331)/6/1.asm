.model small
.stack 100h


.data
        
        array db 3 dup(1)
              db 3 dup(2)
              db 3 dup(3)
              db 3 dup(4) 
              
              
        target db 4 dup(?)
               db 4 dup(?)
               db 4 dup(?)
                    
        

.code


main proc
        
        mov ax,@data
        mov ds,ax
        
        
        mov si,0
        mov di,0
        mov bx,9
        
        for:              
            mov al,array[si]
            mov target[di],al
            add si,3 
            inc di 
            
            cmp si,bx
            ja mid
            
            cmp si,11
            ja end
            
            jmp for
            
            
        mid:
            sub si,11
            inc bl   
            jmp for     
               
                       
        
       end:
            hlt 
        
        
    
endp main
end main