.model small
.stack 100h


.data
        predWord db "a,that$" 
        input db "is a and that stuffs$"
        output db 50 dup (?)
        w1 db ?
        garbage db ? 
        w2 db ?


.code


main proc 
    
        mov ax,@data
        mov ds,ax
            
        mov si,0
            
        l1:
            mov al,predWord[si]
            mov w1[si],al
            inc si
            cmp al,','
            jnz l1
        
            
        mov di,0
            
            
        l2:
            mov al,predWord[si]
            mov w2[di],al
            inc si
            inc di
            cmp al,'$'
            jnz l2 
            
        mov w1[1],'$'
        
        ;word transfer done
        
        mov si,0
        mov di,0
        
        mainLoop: 
            mov al,input[si]
            
            cmp al,w1[0]
            jz stringCheckA
            
            cmp al,'t'
            jz stringCheckB
            
            cmp al,'$'
            jz end
            
            
        mid:    
            mov output[di],al 
            inc si   
            inc di
            jmp mainLoop
            
            
                
            
        stringCheckA:
            
            inc si
            mov bl,input[si] 
            dec si
            cmp bl,20h 
            jz execution
            
              
            jmp mid  
            
            
            
        stringCheckB:
            mov bl,input[si+1h]
            cmp bl,'h'
            jnz mid
                
            mov bl,input[si+2h]
            cmp bl,'a'
            jnz mid
            
            mov bl,input[si+3h]
            cmp bl,'t'
            jz execB
            
            jmp mid
            
            
            
            
        execution:
            inc si
            inc si
            jmp mainLoop 
            
            
        execB:
            inc si
            inc si
            inc si
            inc si
            inc si
            jmp mainLoop 
        
        end:
            hlt          
            
          
        
    
endp main
end main