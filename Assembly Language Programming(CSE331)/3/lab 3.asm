.model small
.stack 100h

.data


.code 

add_two proc

	pop bx			; for absorbing the garbage value and to get the return address  
	pop ax
	pop dx
	add ax,dx         
	push bx         ; for pushing the return address back to the stack 
	
	ret				; to return and terminate
endp add_two	

main proc
	
	push 5
	push 6 
	
	
	mov al,2
	mov bl,1 
	a:
	add al,bl
	jmp b      		;unconditional jump    
	
	
	jz some label	;jump if zero   
	jnz some label	;jump if not zero
	     
	mov ax,bx
	     
	b:
	jmp d           ;to break immaturely 
	
	d:
	hlt 			; to halt the program	
	
	call add_two	;calling the procedure
	
	
endp main			;terminate the procedure not the program
end main