import cv2
import time

index_to_try = 0
print(f"正在嘗試開啟相機索引: {index_to_try}")
cap = cv2.VideoCapture(index_to_try)
time.sleep(1)

if not cap.isOpened():
    print(f"錯誤：無法開啟相機索引 {index_to_try}")
    exit()

# --- 新增：嘗試設定 FOURCC 為 BGR3 ---
# 注意 BGR3 的 FOURCC 可能就是 0 或需要特殊處理，但我們先試試標準方式
fourcc = cv2.VideoWriter_fourcc(*'BGR3') 
print(f"嘗試設定 FOURCC 為: BGR3")
set_fourcc_ok = cap.set(cv2.CAP_PROP_FOURCC, fourcc)
if not set_fourcc_ok:
    print("警告: 設定 FOURCC (BGR3) 失敗")
# --- 設定 FOURCC 結束 ---

# --- 保持設定解析度 (如果之前有效的話) ---
desired_width = 640
desired_height = 480
print(f"嘗試設定解析度為: {desired_width}x{desired_height}")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)
actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"實際讀取到的設定後解析度: {int(actual_width)}x{int(actual_height)}")
# --- 解析度設定結束 ---

print(f"成功開啟相機索引 {index_to_try}！按 'q' 鍵關閉視窗。")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        # print("無法讀取畫面...") # 暫時關閉重複訊息
        time.sleep(0.1)
        continue

    # 在顯示前檢查一次 shape
    # if 'frame_shape' not in locals(): # 只印第一次
    #      frame_shape = frame.shape
    #      print(f"迴圈中讀取到的 Frame Shape: {frame_shape}")

    cv2.imshow('Camera Test - BGR3?', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("程式結束。")


