.model small
.stack 100h



.data
         value db "Hi!Hi,Hi.I$" 
         raw db ? 
         target db ?



.code

main proc
        
        mov ax,@data
        mov ds,ax
        
        mov si,0
        mov di,0
        
        l1:
            mov al,value[si]
            
            cmp al,"$"
            jz end
            
            
            mov target[di],al 
            
            cmp al,2ch
            jz copy 
            
            cmp al,21h
            jz copy
            
            cmp al,2eh
            jz copy 
            
            inc di 
            inc si
            jmp l1
            
            
        copy:
            inc di
            mov target[di],20h
            inc di   
            inc si
            jmp l1
            
            
        end:
            hlt        
        
        
        
    
endp main
end main