4.8.4. 임의의 인자 목록
마지막으로, 가장 덜 사용되는 옵션은 함수가 임의의 개수 인자로 호출될 수 있도록 지정하는 것입니다. 이 인자들은 튜플로 묶입니다 (튜플과 시퀀스 을 보세요). 가변 길이 인자 앞에, 없거나 여러 개의 일반 인자들이 올 수 있습니다.

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
Normally, these variadic arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function. Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments.

>>>
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
4.8.5. 인자 목록 언 패킹
인자들이 이미 리스트나 튜플에 있지만, 분리된 위치 인자들을 요구하는 함수 호출을 위해 언 패킹 해야 하는 경우 반대 상황이 벌어집니다. 예를 들어, 내장 range() 함수는 별도의 start와 stop 인자를 기대합니다. 그것들이 따로 있지 않으면, 리스트와 튜플로부터 인자를 언 패킹하기 위해 *-연산자를 사용해서 함수를 호출하면 됩니다:

>>>
list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
같은 방식으로 딕셔너리도 **-연산자를 써서 키워드 인자를 전달할 수 있습니다:

>>>
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

-----> slicing과 unpacking이 자료를 뽑아오는 형태로 관념이 비슷한데 활용 욜례에 대해 어떠한 차이를 갖나요???
