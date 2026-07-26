# sync.ps1
# 변경된 파일 목록 가져오기
$files = git status --porcelain | ForEach-Object {
    $_.Substring(3)
}

# 파일명이 없으면 종료
if (-not $files) {
    Write-Host "변경된 파일 없음"
    exit
}

# 파일명들을 한 줄로 묶기
$msg = "auto sync: " + ($files -join ", ")

git add .
git commit -m "$msg"
git push origin main
