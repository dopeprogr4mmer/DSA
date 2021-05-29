def maxA(N):
    if (N <= 6):
       return N
    
    # An array to store result of
    # subproblems
    screen = [0] * N
    
    # Initializing the optimal lengths
    # array for uptil 6 input
    # strokes.
         
    for n in range(1, 7):
        screen[n - 1] = n

    # Solve all subproblems in bottom manner
    for n in range(7, N + 1):
             
            # for any keystroke n, we will need to choose between:-
            # 1. pressing Ctrl-V once after copying the
            # A's obtained by n-3 keystrokes.
    
            # 2. pressing Ctrl-V twice after copying the A's
            # obtained by n-4 keystrokes.
    
            # 3. pressing Ctrl-V thrice after copying the A's
            # obtained by n-5 keystrokes.
        screen[n - 1] = max(2 * screen[n - 4],
                        max(3 * screen[n - 5],
                            4 * screen[n - 6]));

    return screen[n-1]


if __name__ == '__main__':
	try:
		#string = 'babcde'
		count=maxA(11)
		print(count)
	except Exception:
		errorno = 50159747054
		print(f"Hey Phantom, there's a {errorno: #x} error")

