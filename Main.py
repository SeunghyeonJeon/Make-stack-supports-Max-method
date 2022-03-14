class Stack:
	def __init__(self):
		self.items =[]
		
	def push(self, val):
		self.items.append(val)
		
	def pop(self):
		try:
			return(self.items.pop())
		except IndexError:
			print("EMPTY")
			
	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("EMPTY")
			
	def __len__(self):
		return len(self.items)
	
	def isEmpty(self):
		return self.__len__() == 0
# 기존의 Stack 클래스 정의

S = Stack()
Max_S = Stack()
# 2개의 stack을 정의합니다. 
# S 스택은, 일반적인 값을 저장하고, Max_S 스택은 실시간으로 입력되는 값들에 대해 크기를 비교하여 큰값을 저장합니다.

while 1:
	var = input().split()
	
	if var[0] == 'push' :
		if(Max_S.isEmpty()):
			Max_S.push(var[1])
			S.push(var[1])
	# 첫 시작과 초기화 되었을 때, Max_S 스택과 S 스택에 입력값을 저장하기 위함
			
		else :
			if(int(var[1]) > int(Max_S.top())) :
				Max_S.push(var[1])
				S.push(var[1])
			else :
				Max_S.push(Max_S.top())
				S.push(var[1])
	# Max_S 에 기존에 값이 존재한다면, 입력값과 비교하여 입력값이 클 경우 그 값을 push하고, 아니라면 기존에 있던 값을 한번더 push 하는 형태의 알고리즘을 작성
	# push method 의 경우 조건문만 활용하였기에 수행시간에 영향을 미치지 않으므로 O(1) 시간에 작동한다고 보았음
	
	elif var[0] == 'pop' :
		val1 = S.pop()
		if(val1 is None) :
			continue
		else:
			Max_S.pop()
			print(val1)
	# pop method의 경우 Max_S의 관리를 위하여 양 스택 모두에서 pop을 해주어야 했다.
	# 53~57번줄의 경우 위의 작성해놓은 Stack class에서 비어있을 때 except처리를 하여 EMPTY를 두번 띄우게 되므로, 위와 같이 예외처리를 하였음
	# pop method의 경우도 위와 마찬가지로 조건문만 활용하여 O(1) 시간에 동작한다고 보았음.
		
	elif var[0] == 'max' :
		val2 = Max_S.top()
		if(val2 is None) :
			continue
		else:
			print(val2)
	# max method는 관리한 Max_S 스택에서 가장 위의 값을 top을 활용하여 보여주면 되겠다고 판단하였음
	# 64~67 line은 pop과 같이 Stack class에서 프린팅되는 EMPTY값에 대한 예외처리를 위해 적어놓았음
	# 조건문만 활용하였기에 O(1) 시간에 동작
	

	elif var[0] == 'exit' :
		break

