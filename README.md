# Rasa Chatbot Project

## Giới thiệu
Đây là một dự án chatbot sử dụng Rasa để xử lý ngôn ngữ tự nhiên (NLU) và quản lý hội thoại (Core). Dự án này giúp xây dựng một trợ lý ảo có thể tương tác với người dùng.

## Cài đặt

### 1. Yêu cầu
- Python 3.8 hoặc cao hơn
- pip
- Rasa Open Source

### 2. Cài đặt Rasa
Bạn có thể cài đặt Rasa bằng lệnh sau:

```bash
pip install rasa
```


### 3. Khởi tạo dự án
#### Nếu project đã có các file rồi thì ko cần thực hiện nữa (Kiểm tra cấu trúc thư mục)
```pycon
rasa init
```

Điều này sẽ tạo ra cấu trúc thư mục cơ bản cho dự án

### Cấu trúc thư mục

Dự án Rasa sẽ có cấu trúc như sau:

```pycon
ChatbotRASA1/
├── actions/
├── config.yml
├── credentials.yml
├── domain.yml
├── data/
│   ├── nlu.yml
│   └── rules.yml
├── models/
├── tests/
├── main.py
└── venv/
```

## Cấu hình

### 1. config.yml
file này chứa cấu hình cho NLU và Core. Có thể điều chỉnh pipeline và các chính sách tại đây
- đọc thêm: https://rasa.com/docs/rasa/model-configuration/

### 2. nlu.yml
file này chứa dữ liệu huấn luyện cho mô hình NLU. Định nghĩa các intents, entities, slots và các ví dụ tương ứng để mô hình học cách nhận diện chúng.

Ví dụ:
```
nlu:
  - intent: greet
    examples: |
      - hi
      - hello
      - good morning
      - hey there

  - intent: goodbye
    examples: |
      - bye
      - see you later
      - goodbye

  - intent: ask_weather
    examples: |
      - What's the weather like in [London](location)?
      - Tell me the weather in [Paris](location).
      - Is it raining in [New York](location)?
```

1. Intents là mục đích của người dùng khi gửi một câu lệnh. Mỗi intent đại diện cho một hành động mà người dùng muốn thực hiện.
- Ví dụ: greet, ask_weather, book_flight.
2. Examples Các ví dụ là các câu lệnh mà người dùng có thể sử dụng để biểu thị một intent cụ thể. Những ví dụ này giúp mô hình học cách nhận diện intents.
- Cách sử dụng: Các ví dụ được định nghĩa dưới từng intent, giúp mô hình có nhiều ngữ cảnh để học từ đó.

### 3. domain.yml
- Đây là nơi bạn định nghĩa các intents, entities, và responses cho chatbot
- Bạn phải liệt kê lại các intents được định nghĩa từ nlu.yml nếu không sẽ gặp lỗi

Ví dụ:
```
version: "3.0"

intents:
  - greet
  - goodbye
  - ask_weather

entities:
  - location

responses:
  utter_greet:
    - text: "Hello! How can I assist you today?"
  utter_goodbye:
    - text: "Goodbye! Have a great day!"
  utter_weather:
    - text: "I'm checking the weather for you. Please hold on a moment."
  utter_fallback:
    - text: "I'm sorry, I didn't quite understand that. Can you rephrase?"

actions:
  - action_greet
  - action_goodbye
  - action_weather
  - action_fallback

# Optional: Configure session and carry over the state
session_config:
  session_expiration_time: 60  # in minutes
  carry_over_slots_to_new_session: true
```

#### Các thành phần trong file:

- intents: Danh sách các intents mà chatbot có thể nhận diện, ví dụ như chào hỏi, tạm biệt và hỏi về thời tiết.

- responses: Các phản hồi mà chatbot sẽ gửi đến người dùng khi nhận được các intents tương ứng.

- actions: Danh sách các action mà chatbot có thể thực hiện. Những action này cần được định nghĩa trong file actions.py.



- session_config: Cấu hình cho phiên làm việc, cho phép bạn quản lý thời gian hết hạn phiên và khả năng mang theo thông tin giữa các phiên.

### 4. stories.yml
File này định nghĩa các kịch bản hội thoại mà chatbot có thể xử lý

Ví dụ
```
version: "3.0"

stories:
  - story: greet and ask weather
    steps:
      - intent: greet
      - action: utter_greet
      - intent: ask_weather
      - action: action_weather

  - story: goodbye interaction
    steps:
      - intent: goodbye
      - action: utter_goodbye

  - story: unknown intent
    steps:
      - intent: some_unknown_intent
      - action: action_fallback
```

#### Giải thích các phần trong file:

- stories: Danh sách các kịch bản hội thoại. Mỗi kịch bản bắt đầu bằng - story: và tiếp theo là các bước (steps) mà người dùng có thể thực hiện.

- steps: Các bước trong kịch bản:
- intent: Ý định của người dùng mà chatbot cần nhận diện.
- action: Hành động mà chatbot sẽ thực hiện sau khi nhận diện được intent.

### Huấn luyện mô hình

Sau khi cấu hình xong, có thể huấn luyện mô hình với lệnh:

```bash
rasa train
```

### Chạy chatbot
- Chức năng: sẽ lấy mô hình mới nhất được train ở `models` để chạy giao diện dòng lệnh cho chatbot, cho phép người dùng tương tác với toàn bộ mô hình
```bash
rasa shell
```

### Kiểm tra khả năng nhận diện intents
- Chức năng: Khởi động một giao diện dòng lệnh chỉ cho phần NLU của mô hình, cho phép người dùng kiểm tra khả năng nhận diện intents mà không xử lý các hành động liên quan tới hội thoại.
- Đặc điểm: Hiển thị thông tin chi tiết về dự đoán của NLU, bao gồm độ tự tin (confidence) và các intent đã nhận diện.

```bash
rasa shell nlu
```

### Tương tác với API của rasa

```bash
rasa run --enable-api --debug --cors "*"
```

