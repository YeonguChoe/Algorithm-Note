# Hackerrank CPP 세팅

## Stream
- Definition: sequence of data that is transferred between a program and an input or output source, such as a file, keyboard, or network connection.

### ofstream
- output_file_stream_object << "내용"와 같은 코드는 출력 스트림에 "내용" 문자열과 개행문자를 기록한다. 이 때, 실제 파일에 쓰기 작업이 발생하지 않고, 데이터는 출력 스트림의 버퍼에 임시로 저장된다.
- 버퍼의 내용이 실제 파일에 쓰여지는 시점은 몇 가지 경우에 발생합니다:
  - 출력 스트림 객체가 파괴될 때 (예: 함수가 끝날 때)
  - 버퍼가 가득 찼을 때
  - 명시적으로 flush() 함수가 호출될 때
  - std::endl를 사용할 때 (output_file_stream_object << std::endl)

```cpp
#include <iostream>
#include <fstream>

ofstream output_file_stream_object("파일이름.txt"); // 객체와 파일 자원을 연결한다.
output_file_stream_object << "파일에 쓸 내용" << std::endl; // 데이터를 버퍼에 기록 한다.
output_file_stream_object.flush(); // 데이터를 버퍼에서 파일로 실제로 전송을 하고 기록한다.
output_file_stream_object.close(); // 파일을 닫아서 파일 자원을 해제한다.
```

## getenv("환경변수 이름")
```cpp
char* home_path = getenv("HOME");
```

