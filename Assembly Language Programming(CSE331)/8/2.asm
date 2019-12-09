.model small
.stack 100h



.data
        input db "computer Programming$"
        

.code



main proc 
    
        mov ax,@data
        mov ds,ax
        
        mov si,0
        
        loop1:
               
            mov al,input[si]
            
            
            cmp al,'a'
            jz change 
            
            cmp al,'e'
            jz change 
            
            cmp al,'i'
            jz change 
            
            cmp al,'o'
            jz change 
            
            cmp al,'u'
            jz change 
            
            cmp al,'$'
            jz end
            
            inc si
            jmp loop1
            
        change:
            sub al,32
            mov input[si],al
            inc si
            jmp loop1  
            
        
        end:
            hlt    
                   
        
        
        
        
    
    
    
endp main
end main