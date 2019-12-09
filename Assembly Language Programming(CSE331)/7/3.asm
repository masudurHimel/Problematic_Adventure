.model small
.stack 100h


.data
         target db 1,2,3,4,10,5,12,7,8,9
         value db ?

.code

main proc 
    
        mov ax,@data
        mov ds,ax 
        
        
        mov si,0
        
        mov al, target[si]
        
        l1:
            inc si
            cmp si,10
            jz end
            
            mov bl,target[si]
            cmp al,bl  
            jl mid
            
            jmp l1
            
            
        mid:
            mov al,bl 
            jmp l1
            
            
        end:
            mov value,al
            hlt        
            
            
            
        
        
        
    
    
endp main 
end main