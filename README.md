# Decision_Tree_Testing

| **Title**      | Decision Tree: Tìm nguyên nhân khách hàng bị nợ xấu|
| ---------- |-------------------|
| **Team**       | Nguyễn Phước Tân <nptan2005@gmail.com>, Tiết Hán Cường <cuongth3650@gmail.com>|
| **Predicting** | Mục tiêu tìm nguyên nhân những khách hàng vay tín dụng bị nhảy nhóm nợ. Từ đó đưa ra chính sách thay đổi để giảm thiểu khách hàng nợ xấu|
| **Data**       | Dữ liệu giả lặp về thông tin khách hàng bao gồm: Mã khách hàng và các tham số liên quan như: tuổi, ngày đáo hạn, ngày khách hàng nhận lương, nghề nghiệp, loại hình sản phẩm, tỉnh thành cư trú, hạn mức, dư nợ ($ dolar), tỷ lệ sử dụng, tỷ lệ sử dụng bình quân,.. **(dữ liệu là giả lặp nhưng được random dựa trên 1 số trọng số thực tế như tỷ lệ nợ trên 1 nhóm khách hàng)**|
| **Features**   |1. Ngày đáo hạn và ngày nhận lương: nhận thấy rằng nếu ngày nhận lương quá xa ngày đáo hạn, có thể khách hàng sẽ không còn đủ tiền trả nợ
|                |2.ỷ lệ sử dụng bình quân (dư nợ bình quân/hạn mức được cấp): nhận thấy rằng khách hàng có tỷ lệ lớn, dư nợ kéo dài và ít có chiều hướng giảm => khả năng khách hàng này mất khả năng chi trả trong tương lai
|                |3.Tuổi: xét về tuổi lao động khách hàng
|                |4.Thu nhận năm: xét về thu nhập khách hàng so với khoảng nợ đang vay|
| **Models**     | DecisionTreeClassifier và RandomForestClassifier, so sánh kết quả của 2 model|
| **Results**    | |
| **Discussion** | This is where you share your thoughts about your project. (Hopefully you have a few interesting interpretations!) Briefly summarized what just happened. Briefly explain whether or not you expected your results. If your results were good, explain why. If they were not good, explain why. **(6 sentences max)**|
| **Future**     | If you had another 6 months to work on this, what would you do first? **(2-3 sentences max)**|
|**References**  |[IEEE style](https://ctan.org/topic/bibtex-sty?lang=en) is fine|

