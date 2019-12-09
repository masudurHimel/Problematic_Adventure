.model small
.stack 100h



.data
    
    array db 16 dup(?) 
    inputArray db ?
    avg db ?
    lowest db ?
    highest db ?


.code


main proc
    
    mov ax,@data
    mov ds,ax 
    
    mov dl,0
     
    loop:
        mov ah,01
        int 21h
        
        inc dl
        cmp dl,32
        jz copy
        
        cmp al,20h
        jz loop
        
        mov ah,0
        sub al,30h
        push ax
          
        jmp loop
                
                
    copy:
    
       mov si,0
       
       for:
            pop ax
            mov inputArray[si],al
            inc si 
            
            cmp si,17 
            jz average
            
            jmp for
            
            
            
    average:
    
        mov si,0
        mov al,0
        
        l1:
           mov bl,inputArray[si]
           add al,bl
           
           inc si
           cmp si,17         
           jz averageResult
           
           jmp l1
           
           
           
    averageResult:
    
        mov ah,0
        mov cl,16
        div cl
        
        mov avg,al   
        
        jmp low
        
        
    low:
    
        mov si,0 
        mov di,1
         
        l2:
           mov al,inputArray[si]
           
           l3:
              mov bl,inputArray[di]
              cmp al,bl
              ja lowMid
              
              inc di
              
              cmp di,16
              jz lowResult
               
              jmp l3
              
              
              
              
              
    lowMid:
        
        mov al,bl  
        inc di
        
        cmp di,16
        jz lowResult
                   
        jmp l3 
        
        
        
    lowResult:
    
        mov lowest,al 
        
        
                 
    high:
    
        mov si,0 
        mov di,1
         
        lh2:
           mov al,inputArray[si]
           
           lh3:
              mov bl,inputArray[di]
              cmp al,bl
              jb highMid
              
              inc di
              
              cmp di,16
              jz highResult
               
              jmp lh3
              
              
              
              
              
    highMid:
        
        mov al,bl  
        inc di
        
        cmp di,16
        jz highResult
                   
        jmp lh3 
        
        
        
    highResult:
    
        mov highest,al 
        
        
           
               
        
        
    end:
        hlt     
        
        
        
    
             
    
    
endp main
end main