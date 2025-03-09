# AI Agent Chat

A modern chat interface application that connects to Ollama LLM models, built with Flet framework.

## Features

- Clean, responsive UI with animated components
- Integration with Ollama LLM models (currently using qwen2.5-coder:1.5b)
- Message history display with AI and user messages
- Loading animation while waiting for AI responses
- Collapsible navigation panel

## Installation

### Requirements

- Python 3.8+
- Ollama installed and running locally

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-agent-chat.git
cd ai-agent-chat
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python main.py
```

## Project Structure

- `main.py` - Application entry point
- `app/` - Main application package
  - `animations/` - Animation utilities
  - `components/` - UI components (Header, MessageCard, Loading)
  - `model_llm/` - LLM integration with Ollama
  - `providers/` - Screen state management
  - `screens/` - Application screens (Home, Navigation)

## Usage

1. Type your question in the text field at the bottom of the screen
2. Click the send button or press Enter
3. Wait for the AI response
4. Use the menu button in the header to collapse/expand the navigation panel

## Technologies

- [Flet](https://flet.dev/) - Flutter-powered UI framework for Python
- [LangChain](https://www.langchain.com/) - Framework for LLM application development
- [Ollama](https://ollama.ai/) - Run LLMs locally

---

# AI Agent Chat

Ứng dụng giao diện trò chuyện hiện đại kết nối với mô hình Ollama LLM, được xây dựng bằng framework Flet.

## Tính năng

- Giao diện người dùng đẹp, đáp ứng với các thành phần hoạt ảnh
- Tích hợp với mô hình Ollama LLM (hiện đang sử dụng qwen2.5-coder:1.5b)
- Hiển thị lịch sử tin nhắn với AI và người dùng
- Hoạt ảnh loading khi đợi phản hồi từ AI
- Bảng điều hướng có thể thu gọn

## Cài đặt

### Yêu cầu

- Python 3.8+
- Ollama đã được cài đặt và chạy trên máy

### Thiết lập

1. Clone repository:
```bash
git clone https://github.com/yourusername/ai-agent-chat.git
cd ai-agent-chat
```

2. Tạo môi trường ảo và kích hoạt:
```bash
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
```

3. Cài đặt các phụ thuộc:
```bash
pip install -r requirements.txt
```

## Chạy ứng dụng

```bash
python main.py
```

## Cấu trúc dự án

- `main.py` - Điểm vào của ứng dụng
- `app/` - Gói ứng dụng chính
  - `animations/` - Tiện ích hoạt ảnh
  - `components/` - Các thành phần UI (Header, MessageCard, Loading)
  - `model_llm/` - Tích hợp LLM với Ollama
  - `providers/` - Quản lý trạng thái màn hình
  - `screens/` - Các màn hình ứng dụng (Home, Navigation)

## Cách sử dụng

1. Nhập câu hỏi của bạn vào ô văn bản ở dưới cùng màn hình
2. Nhấp vào nút gửi hoặc nhấn Enter
3. Đợi phản hồi từ AI
4. Sử dụng nút menu trong tiêu đề để thu gọn/mở rộng bảng điều hướng

## Công nghệ

- [Flet](https://flet.dev/) - Framework UI sử dụng Flutter cho Python
- [LangChain](https://www.langchain.com/) - Framework phát triển ứng dụng LLM
- [Ollama](https://ollama.ai/) - Chạy các mô hình LLM cục bộ
