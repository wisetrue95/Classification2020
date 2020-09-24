# ImageNet2012 Dataset Preprocessiong

# 1. ImageNet2012 Dataset Download

- official site : [http://image-net.org/download](http://image-net.org/download)
- torrent file download : [https://academictorrents.com/collection/imagenet-2012](https://academictorrents.com/collection/imagenet-2012)
- 참고 github : [https://github.com/developer0hye/Setup-for-Imagenet](https://github.com/developer0hye/Setup-for-Imagenet)

공식 사이트 승인을 받을려면 3~5일 정도 기다려야 해서, 토렌트 파일로 다운로드 했다.

원래 파일이 train/val/test 각각 있으나, test 파일은 라벨링이 되어 있지 않아 보통 val파일로 테스트를 적용했다.

1. validation 폴더는 이미지가 폴더별로 정리되어 있지 않아 train폴더 같이 정리가 필요하다.

    - train set 예시

        ![ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Untitled.png](ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Untitled.png)

    - val 예시

        ![ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Untitled%201.png](ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Untitled%201.png)

    - Imagenet_val_setup.sh 를 실행하면 Val 폴더 역시 train 폴더 같이 폴더별로 정리된다.

        ( 해당 파일은 첫번째 참고 github 주소에 업로드 되어 있음)

        [Imagenet_val_setup.sh](ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Imagenet_val_setup.sh)

# 2. ImageNet2012 Preprocessing

- 학습 편의를 위해 왼쪽과 같이 된 폴더명을 클래스 명으로 각 변경한다.
- 폴더명 - 클래스 정수형 - 클래스명 map 파일

    [map_clsloc.txt](ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/map_clsloc.txt)

- 참고

[How to prepare Imagenet dataset for Image Classification - A Developer Diary](http://www.adeveloperdiary.com/data-science/computer-vision/how-to-prepare-imagenet-dataset-for-image-classification/)

- issue 1 : crane 중복
    - 변경

        ![ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Untitled%202.png](ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Untitled%202.png)

- issue 2: maillot 중복
    - 변경

        ![ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Untitled%203.png](ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Untitled%203.png)

- imagenet_data_prep.py
- 이미지넷 데이터는 폴더명이 n03857828 이런식으로 분류되어 있다. 폴더명을 라벨명으로 변환 해줘야 한다.
- 또한 기존 이미지넷 test파일은 라벨링이 되어 있지 않아, train에서 일부 각 클래스당 50개씩 빼와서 test폴더를 만들어 준다.



- 실행 전→후

![ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Untitled%204.png](ImageNet2012%20Dataset%20Preprocessiong%20877fcf7b8ed94267a2368f55e47e50f6/Untitled%204.png)

# 3. Convert to TFRecord

```bash

```
