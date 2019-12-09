.model small
.stack 100h


.data            

    stringRaw db ? 
    stringRaw1 db ?
    stringRaw2 db ? 
    stringRaw3 db ?  
    stringRaw4 db ? 
    
    targetString db ?
    index db 0


.code


main proc  
    
        mov ax,@data
        mov ds,ax  
        
        mov si,0
        
        stringLoop:
            mov ah,01
            int 21h
            
            cmp al,13
            jz target
            
            mov stringRaw[si],al
            inc si
              
            jmp stringLoop  
                              
                              
        
        target:
            
            
            
            mov ah,02
            mov dl,10
            int 21h
            
            mov ah,02
            mov dl,13
            int 21h 
            
            
            mov ah,01
            int 21h
     
           
            mov targetString[0],al 
            
            mov ah,01
            int 21h
            
            cmp al,0dh
            jz search
            
            
        search: 
             mov si,0
             mov bl,targetString 
             
             searchLoop:
                    mov al, stringRaw[si]
                    cmp al,bl
                    jz result
                     
                    inc si 
                    cmp si,6
                    jz end  
                    
                    jmp searchLoop
                      
                    
          
        result:
            mov ax,si
            mov index[0],al 
            jmp end 
            
        end:          
            hlt      
        
    
    
endp main
end main