import asyncio, os
import platform

async def create_subprocess(cmd):
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    while True:
        stdout = (await proc.stdout.readline()).decode('cp65001', 'ignore').rstrip()
        if len(stdout):
            print(stdout, end='\n', flush=True)
        else:
            break

async def main():
    if platform.system() == 'Windows':
        activate = '.\\venv\\Scripts\\activate.bat'
    elif platform.system() == 'Darwin':
        activate = './venv/bin/activate'
    else:
        raise Exception('Unsupported OS')
    await create_subprocess('python -m venv venv')
    await create_subprocess(f'{activate} && python -m pip install --upgrade pip && pip install -r requirements.txt')
    os.system('PAUSE')

try:
    asyncio.run(main())
except Exception as e:
    print(e)
    os.system('PAUSE')