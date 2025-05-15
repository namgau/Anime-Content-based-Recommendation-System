I. Lưu ý khi chạy file ipynb:
	- 2 file csv là tập data
 	- Label tốt hay xấu được đánh giá dựa trên mục Pos_Feedback_Cnt

II. Yêu cầu khi chạy file "dashboard":
	1. Yêu cầu hệ thống & thư viện
		Hệ thống
		Python >= 3.8
		Trình duyệt hiện đại (Chrome, Firefox, Edge,...)
		Cài đặt thư viện (qua pip)
		pip install streamlit pandas plotly wordcloud scikit-learn matplotlib
	2. Cách chạy ứng dụng
		Tải file dữ liệu: Đảm bảo đã có file "Nhóm-7-Women_Clothes_Data.csv" trong cùng thư mục.
		Chạy Streamlit app:
		streamlit run ten_file_dashboard.py
	3. Hướng dẫn sử dụng dashboard
		Sidebar - Bộ lọc
		Chọn Label: Lọc theo review Tốt (≥6 vote tích cực) hoặc Xấu (<6).	
		Chọn độ dài review: Giới hạn khoảng độ dài để phân tích tập trung hơn.	
	4. Mô tả chức năng và biểu đồ
		Tab 1: Tổng quan
		Số lượng review: Tổng số review theo bộ lọc.
		Phân bố độ dài review: Biểu đồ histogram giúp biết các review dài/ngắn ra sao.
		Tỉ lệ các Label: Biểu đồ tròn mô tả tỉ lệ giữa review Tốt và Xấu.
		Tab 2: WordCloud & Từ khóa
		WordCloud toàn bộ: Tổng hợp từ ngữ xuất hiện nhiều nhất trong toàn bộ review.
		WordCloud theo Tốt/Xấu: So sánh từ phổ biến trong hai loại review.
		Từ khóa phổ biến: Bảng liệt kê top 30 từ có tần suất cao trong mỗi nhóm review (Tốt và Xấu).
		Tab 3: Từ khóa phổ biến (theo bộ lọc)
		Bảng liệt kê các từ xuất hiện thường xuyên nhất trong các review đã lọc.
	5. Chuẩn bị bản demo cuối cùng
		Kiểm thử và tối ưu:
		Đã test chạy mượt với dữ liệu ~9400 review.
		Tương thích với nhiều trình duyệt (đã test trên Chrome, Brave và Firefox).
		Giao diện responsive tương đối, xem được cả trên laptop và tablet.# idk
