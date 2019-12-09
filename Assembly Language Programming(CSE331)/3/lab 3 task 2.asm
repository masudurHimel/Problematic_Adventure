.model small
.stack 100h

.data

	
	string1 db "Hello world$"
	string2 db "this is Assembly Language Programming$"   
	string3 db ?
	
	count db 0 
	i db 0

.code  



main proc
            
 	mov ax, @data
	mov ds,ax
	

	lea si, string1
    mov bx, 0
    mov al,[si+bx]
    mov cx,0
    ;cmp al,0
    jnz first
  ;  jz exit

    
    first:      
    
   	mov string3[bx],al
   	add bx,1
   	mov al,[si+bx]
   	cmp al,"$"
   	jnz first 
   	jz mid    
   	
   	
   	mid:
   	add i,11d
   	lea si, string2
    mov bx, 0
    mov al,[si+bx]
    mov cx,0
    ;cmp al,0
    jnz second
  ;  jz exit
  
  	second:
  	mov string3[bx+11],al
   	add bx,1
   	mov al,[si+bx]
   	cmp al,"$"
   	jnz second 
   	hlt
   	  


   	
   	     
   	

   	
   	
    

   
         
         
         
         
endp main
end main
