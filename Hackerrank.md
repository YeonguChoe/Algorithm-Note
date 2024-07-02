# Hackerrank CPP 세팅

## Stream
- Definition: sequence of data that is transferred between a program and an input or output source, such as a file, keyboard, or network connection.

### ofstream
```cpp
ofstream output_file_stream_object("파일이름.txt"); // 객체와 파일 자원을 연결한다.
/**
*"output_file_stream_object << "내용" " 이 코드를 실행하면, 먼저 "내용" 문자열과 개행 문자가 출력 스트림의 버퍼에 기록됩니다. 실제 파일에 쓰기: 버퍼가 일정 크기가 되거나, std::endl을 만나면 버퍼의 내용이 실제 파일에 쓰여집니다. 이 과정을 "flush"라고 합니다.
*/
output_file_stream_object << "파일에 쓸 내용" << std::endl; // 데이터를 버퍼에 기록 한다.
output_file_stream_object.flush(); // 데이터를 버퍼에서 파일로 실제로 전송을 하고 기록한다.
output_file_stream_object.close(); // 파일을 닫아서 파일 자원을 해제한다.
```

## getenv("환경변수 이름")
```cpp
char* oa_path = getenv("HOME");
```

