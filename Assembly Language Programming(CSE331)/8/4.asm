.model small
.stack 100h



.data
    input db 7,4,2,5,0
    even db 5 dup(200)
    odd db 5 dup(200) 
    
    sortedEven db 5 dup(200)
    sortedOdd db 5 dup(200)


.code


main proc
        mov ax,@data
        mov ds,ax  
        
        mov si,0
        mov di,0
        
        l1:
            mov al,input[si]
            mov cl,al
            mov ah,0
            inc si
            
            cmp si,6
            jz mid
            
            mov bl,2
            div bl
            cmp ah,0
            jnz l1
            

            
            mov even[di],cl
            inc di
            jmp l1
            
            
           
                  
                  
        mid:
            mov even[di],'$'
            mov si,0
            mov di,0   
            
        
        l2:
            mov al,input[si]
            mov cl,al
            mov ah,0
            inc si
            
            cmp si,6
            jz mid2
            
            mov bl,2
            div bl
            cmp ah,0
            jz l2 
            
            mov odd[di],cl
            inc di
            jmp l2
            
            
        mid2:
            mov odd[di],'$'
            mov si,0
            mov di,0
            
            
        evenSort:
            mov al,even[si]
            mov bl,sortedEven[di] 
            
            
            cmp al,bl
            jb evenShiftMid 
            
            cmp al,'$'
            jz mid3
            
            jmp evenSort
            
            
            
        evenShiftMid:
            mov dx,di  
            mov di,2
            jmp evenShift
            
        evenShift:
            
            mov cl,sortedEven[di]
            mov sortedEven[di+1h],cl
            
            cmp di,dx  
            jz evenShiftEnd
            dec di
            jmp evenShift
            
        evenShiftEnd:
            mov di,dx
            mov sortedEven[di],al
            inc si
            mov di,0
            jmp evenSort            
            
        
        
        
        mid3:
            
            mov si,0
            mov di,0
            
            
        oddSort:
            mov al,odd[si]
            mov bl,sortedOdd[di] 
            
            
            cmp al,bl
            jb oddShiftMid 
            
            cmp al,'$'
            jz end
            
            jmp oddSort
            
            
            
        oddShiftMid:
            mov dx,di  
            mov di,1
            jmp oddShift
            
        oddShift:
            
            mov cl,sortedOdd[di]
            mov sortedOdd[di+1h],cl
            
            cmp di,dx  
            jz oddShiftEnd
            dec di
            jmp oddShift
            
        oddShiftEnd:
            mov di,dx
            mov sortedOdd[di],al
            inc si
            mov di,0
            jmp oddSort            
            
        
        
        
            
        end: 
            
            hlt        
            
            
        
        
        
        
    
    
endp main
end main