.model small
.stack 100h


.data
     
     binaryValue db 10110101b 
     count db 0

.code                       

main proc
        
        mov ax,@data
        mov ds,ax
        
        mov cl,1 
        mov si,0
        mov al,binaryValue 
        
        loop:
            shl al,cl
            jc mid
                    
            inc si        
            cmp si,9
            jz end
            
            jmp loop 
            
            
        mid:
            mov bl,count
            inc bl 
            mov count,bl
            
            jmp loop
            
        end:
            hlt        
    
    
endp main
end main