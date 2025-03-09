# AI Agent Chat sử dụng Ollama, LangChain, FletUI Python

![](./docs/imgs/bg.png)

[Video hướng dẫn chi tiết](https://youtu.be/vW4WP8lEE7g)

[Website](https://syncdev8.com)

Ứng dụng giao diện trò chuyện hiện đại kết nối với mô hình Ollama LLM, được xây dựng bằng framework Flet.

## Tính năng

### Giao diện người dùng
- Thiết kế hiện đại với giao diện đáp ứng sử dụng Flet UI
- Các thành phần có hoạt ảnh mượt mà (scale, fade, slide) 
- Bảng điều hướng có thể thu gọn/mở rộng với animation
- Hiển thị avatar và biểu tượng cho người dùng/AI
- Giao diện chat dạng bubble messages phân biệt người dùng/AI

### Tích hợp AI
- Sử dụng mô hình Ollama LLM qwen2.5-coder:1.5b
- Xử lý prompt template thông minh với LangChain
- Cache kết quả trả về để tối ưu hiệu suất
- Định dạng câu trả lời theo tiêu chí:
  + Chính xác và đầy đủ về mặt nội dung
  + Dễ hiểu và phù hợp ngữ cảnh
  + Đúng ngữ pháp và từ vựng

### Tương tác
- Hiển thị lịch sử chat theo thời gian thực
- Hoạt ảnh loading khi đang chờ phản hồi từ AI
- Hỗ trợ gửi tin nhắn qua nút gửi hoặc phím Enter
- Thanh nhập liệu với placeholder text và biểu tượng cảm xúc
- Cuộn tin nhắn tự động khi có tin nhắn mới

### Cấu trúc mã nguồn
- Tổ chức theo mô hình component-based
- Tách biệt logic xử lý AI và giao diện người dùng
- Sử dụng các design pattern phổ biến
- Code được comment và format rõ ràng

## Cài đặt

### Yêu cầu

- Python 3.8+
- Ollama đã được cài đặt và chạy trên máy

### Thiết lập

1. Clone repository:
```bash
git clone https://github.com/8syncdev/ai-agent-chat.git
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

## Liên hệ

- 🌐 Website: [syncdev8.com](https://syncdev8.com)
- 📱 Facebook: [8sync](https://www.facebook.com/8sync)
- 🎵 Tiktok: [@_8_sync_](https://www.tiktok.com/@_8_sync_)
- 💬 Nhóm Zalo: [Tham gia](https://zalo.me/g/mitxdi486)
- 💻 Github: [8syncdev](https://github.com/8syncdev)
