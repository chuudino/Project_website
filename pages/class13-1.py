import streamlit as st

st.title("Class 13-1")
st.write("Welcome to class 13-1!")
st.markdown("# Welcome to class 13-1!")
st.markdown("## Welcome to class 13-1!")
st.markdown("### Welcome to class 13-1!")
st.markdown(
    '''
您可以使用 **Pydub** 來切割音訊檔案，只保留前 1 分鐘的音訊來測試轉換功能。以下是修改過的程式碼，讓您可以對 M4A 檔案進行切割後再進行語音轉文字處理：

### 切割音訊並轉換的程式碼
```python
import os
import sys
from pydub import AudioSegment
import whisper

# 設定工作目錄為當前腳本所在位置
os.chdir(sys.path[0])

############################ 定義函式 ############################
def convert_and_trim_m4a(input_file, output_file, duration_ms):
    """將 M4A 檔案轉換為 WAV 並切割到指定時間"""
    # 讀取 M4A 檔案
    audio = AudioSegment.from_file(input_file, format="m4a")
    
    # 切割到指定時間（毫秒）
    trimmed_audio = audio[:duration_ms]
    
    # 儲存為 WAV 格式
    trimmed_audio.export(output_file, format="wav")
    print(f"音訊切割並轉檔完成：{output_file}")


def transcribe_with_whisper(audio_file):
    """使用 OpenAI Whisper 進行語音轉文字"""
    model = whisper.load_model("base")  # 選擇模型
    result = model.transcribe(audio_file)
    print("轉錄結果：")
    print(result["text"])
    return result["text"]

############################ 主程式 ############################
# 定義檔案路徑
input_m4a = "D:\\小會研發組2023\\audio20241119 錄音檔.m4a"
output_wav = "audio20241119_trimmed.wav"
duration_ms = 60 * 1000  # 切割為 1 分鐘（60 秒）

# 第一步：將 M4A 檔案切割並轉換為 WAV
convert_and_trim_m4a(input_m4a, output_wav, duration_ms)

# 第二步：使用 Whisper 將 WAV 檔案轉換為文字
transcribe_with_whisper(output_wav)
```

---

### 說明
1. **切割音訊**
   - 使用 `AudioSegment[:duration_ms]` 方法只保留音訊的前 1 分鐘（60,000 毫秒）。
   - 如果想切割其他部分，可以調整時間範圍，例如 `audio[start_ms:end_ms]`。

2. **處理長音訊**
   - 如果原始音檔太大且需要逐段處理，您可以將檔案分割成多個部分，並對每部分分別進行轉錄。

3. **Whisper 模型**
   - Whisper 可直接處理切割後的音訊，因此適合先切割再進行轉錄，避免處理整段音檔過於耗時。

這樣能讓您快速測試程式功能，並確保長音訊也能順利進行語音轉文字轉換！


'''
)
