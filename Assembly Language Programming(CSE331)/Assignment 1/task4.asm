.model small
.stack 100h



.data



.code




main proc
    
        mov di,-1
        
        firstLoop:     ;here I've used two predefined loops for printing the pattern rather than using the builtin loop
        
            inc di
            cmp di,5
            jz end
            mov si,0
            
            
            
            secondLoop:               ;nested loop for printing the pattern
                
                mov ah,02
                mov dl,'*'
                int 21h
                
                cmp si,di
                jz mid
                
                inc si
                
                jmp secondLoop
                
                
        mid:             ; for putting a new line
            mov ah,02
            mov dl,10
            int 21h
            
            mov ah,02
            mov dl,13
            int 21h 
            jmp firstLoop
                    
                
                
        end:
            hlt        
    
    
    
endp main
end main