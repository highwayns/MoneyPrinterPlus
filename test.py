import azure.cognitiveservices.speech as speechsdk

# 设置你的API密钥和服务区域
speech_key = "a28310201b814b688d40c55bbaf082a1"
service_region = "japaneast"

# 创建Speech配置
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# 设置合成语音的语言和声音
speech_config.speech_synthesis_language = "ja-JP"  # 例如，日语
speech_config.speech_synthesis_voice_name = "ja-JP-NanamiNeural"  # 选择特定的声音

# 创建合成器
audio_config = speechsdk.audio.AudioOutputConfig(filename="output.wav")
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# 合成并保存语音
text = "こんにちは、これはテストです。"
result = synthesizer.speak_text_async(text).get()

# 检查结果
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("语音合成成功")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print(f"语音合成取消: {cancellation_details.reason}")
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print(f"错误详情: {cancellation_details.error_details}")
