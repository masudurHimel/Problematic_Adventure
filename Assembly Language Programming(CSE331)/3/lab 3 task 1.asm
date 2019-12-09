.model small
.stack 100h

.data

	string db "Hello world"
	count db 0 
	i db 0

.code  



main proc 
	
	    mov ax, @data
    	mov ds,ax
        
        lea si, string
	    mov bx, 0
	    mov al,[si+bx]
	    jnz a
	    jz exit
	    
	    
	   	a:
	   	add count,1
	   	add bx,1
	   	mov al,string[si+bx]  
	   	sub al,0
	   	jnz a
	   	jz exit


	   	 
	    exit:
	    mov cl,count
	    hlt
	
	
	
endp main
end main