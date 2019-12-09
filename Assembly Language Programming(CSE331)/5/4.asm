.model small
.stack 100h


.data

        marks db 7,6,5,4,7,6,6,8,3,10
        
        
        freqI db 0,1,2,3,4,5,6,7,8,9,10
        frequ db 0,0,0,0,0,0,0,0,0,0

.code


main proc 
       
        mov ax,@data
        mov ds,ax
        
            
        mov si,-1
        mov di,0
                     
        
        firstLoop:
            
            
              
            inc si
            
            cmp si,10
            jz end
            
            mov di,0
            mov al,marks[si]
            
            secondLoop:
            
                cmp di,10
                jz firstLoop
                
                
                mov bl,marks[di]
                cmp al,bl
                jz midF
                
                inc di
                jmp secondLoop
            
            
        midF:
           mov ah,0
           push si
           mov si,ax
           mov dl,frequ[si]
           inc dl
           mov frequ[si],dl
           mov marks[di],-3
           pop si
           inc di
           jmp secondLoop
                         
                         
                         
        end:
            hlt                 
                
                    
            
            
    
    
endp main
end main