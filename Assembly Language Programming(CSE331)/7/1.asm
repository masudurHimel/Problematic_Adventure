.model small
.stack 100h


.data
         
         value db 26
         target db ? 
    



.code

main proc 
    
        mov ax,@data
        mov ds,ax
        
        
        
        mov al,value
        mov ah,0 
        
        mov bl,2
        
        mov dx,"$"
        push dx
        mov si,0
        mov di,0
        
        
        loop1:
            
            div bl
            
            
            mov ch,0
            mov cl,ah
            
            push cx 
            
            cmp al,0
            jz mid
            
            mov ah,0
            
            jmp loop1
            
        
        
        mid:
            mov cx,0
            
            pop ax
            
            
            mov target[si],al
            inc si
            
            cmp ax,"$" 
            jz end
            
            jmp mid
                   
                   
        ;mid2:
;            mov ah,0
;            mov al,target[di]  
;            
;            cmp al,"$"
;            jz end
;            
;            mov bl,10d
;            
;            mul bl
;            
;            add cx,ax
;            
;            inc di
;            jmp mid2
            
             
                  
                
        end:
            hlt              
       
    
    
    
    
    
endp main
end main

