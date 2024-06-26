import json
import os
from elevenlabs import generate, Voice,set_api_key
from videotrans.configure import config
from videotrans.util import tools


def get_voice(*,text=None, role=None, volume="+0%",pitch="+0Hz", rate=None,language=None, filename=None,set_p=True,inst=None):
    try:
        with open(os.path.join(config.rootdir,'elevenlabs.json'),'r',encoding="utf-8") as f:
            jsondata=json.loads(f.read())
        if config.params['elevenlabstts_key']:
            set_api_key(config.params['elevenlabstts_key'])
        audio = generate(
            text=text,
            voice=Voice(voice_id=jsondata[role]['voice_id']),
            model="eleven_multilingual_v2"
        )
        with open(filename,'wb') as f:
            f.write(audio)
        if tools.vail_file(filename) and config.settings['remove_silence']:
            tools.remove_silence_from_end(filename)
        if set_p and inst and inst.precent<80:
            inst.precent+=0.1
            tools.set_process(f'{config.transobj["kaishipeiyin"]} ',btnkey=inst.init['btnkey'] if inst else "")
    except Exception as e:
        error=str(e)
        if set_p:
            tools.set_process(f'elevenlabs:{error}',btnkey=inst.init['btnkey'] if inst else "")
        config.logger.error(f"elevenlabsTTS：request error:{error}")
        if inst and inst.init['btnkey']:
            config.errorlist[inst.init['btnkey']]=error
        raise Exception(error)
    else:
        return True