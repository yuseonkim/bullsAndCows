import cowscheck
import bulls

answer = random()
attempts = 0
print("게임시작!!)
while attempts < 10:
    guess = input (" 네자리 숫자를 입력하세요 : ")
    attempts += i
    if len(guess) != 4 or not guess.isdigt():
	print("잘못된 입력값입니다. 4자리 숫자를 입력해주세요")
	continue
    bulls = do_cowscheck(answer,guess)
    cows = do_cowscheck(answer,guess)
    if bulls == 4:
	print("축하합니다! ", attempts, "번으로 게임을 승리하셨습니다!")
	return
    else:
	print(bulls,"Bulls",cows,"Cows")
print("당신은 패배하였습니다 정답은 ", answer,"였습니다")
