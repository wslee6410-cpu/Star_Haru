<#
============================================================
create_project.ps1
행복로또번호 자동 생성기 프로젝트 폴더 및 파일 자동 생성 스크립트
幸福彩票号码自动生成器项目文件夹及文件自动生成脚本

📌 사용 방법 (使用方法):
   PowerShell에서 이 파일이 있는 폴더로 이동한 후 실행
   在PowerShell中移动到本文件所在文件夹后运行
   .\create_project.ps1

📌 주의사항 (注意事项):
   - 관리자 권한이 필요하지 않습니다 (不需要管理员权限)
   - 이미 존재하는 폴더/파일은 건너뜁니다 (已存在的文件夹/文件会跳过)
   - 실행 후 tree /F 로 구조를 확인할 수 있습니다 (运行后可用 tree /F 查看结构)
============================================================
#>

# ============================================================
# 1. 스크립트 시작 메시지 (脚本开始消息)
# ============================================================
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  🍀 행복로또번호 자동 생성기 프로젝트 생성 스크립트" -ForegroundColor Yellow
Write-Host "  🍀 幸福彩票号码自动生成器项目创建脚本" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# ============================================================
# 2. 프로젝트 루트 폴더 이름 (项目根文件夹名称)
# ============================================================
$PROJECT_NAME = "happy_lotto_generator"

# ============================================================
# 3. 루트 폴더 생성 (创建根文件夹)
# ============================================================
Write-Host "📁 1. 루트 폴더 생성 중... (正在创建根文件夹...)" -ForegroundColor Green
if (-not (Test-Path $PROJECT_NAME)) {
    New-Item -ItemType Directory -Path $PROJECT_NAME | Out-Null
    Write-Host "   ✅ 루트 폴더 생성 완료: $PROJECT_NAME" -ForegroundColor Green
} else {
    Write-Host "   ⚠️ 루트 폴더가 이미 존재합니다: $PROJECT_NAME" -ForegroundColor Yellow
}

# ============================================================
# 4. 루트 폴더로 이동 (进入根文件夹)
# ============================================================
Set-Location -Path $PROJECT_NAME
Write-Host "   📂 현재 위치: (Get-Location)" -ForegroundColor Gray

# ============================================================
# 5. 하위 폴더 생성 (创建子文件夹)
# ============================================================
Write-Host ""
Write-Host "📁 2. 하위 폴더 생성 중... (正在创建子文件夹...)" -ForegroundColor Green

# 생성할 폴더 목록 (要创建的文件夹列表)
$folders = @(
    "config",
    "core",
    "utils",
    "data",
    "data\raw",
    "data\processed",
    "data\output",
    "tests",
    "logs",
    "web",
    "web\templates",
    "web\static"
)

foreach ($folder in $folders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
        Write-Host "   ✅ 폴더 생성: $folder" -ForegroundColor Green
    } else {
        Write-Host "   ⚠️ 폴더 이미 존재: $folder" -ForegroundColor Yellow
    }
}

# ============================================================
# 6. 빈 파일 생성 (创建空文件)
# ============================================================
Write-Host ""
Write-Host "📄 3. 빈 파일 생성 중... (正在创建空文件...)" -ForegroundColor Green

# 생성할 파일 목록 (要创建的文件列表)
$files = @(
    "README.md",
    "requirements.txt",
    "main.py",
    "config\settings.py",
    "core\__init__.py",
    "core\generator.py",
    "core\analyzer.py",
    "core\validator.py",
    "core\database.py",
    "utils\__init__.py",
    "utils\file_io.py",
    "utils\formatter.py",
    "utils\visualizer.py",
    "utils\kakao_sender.py",
    "tests\__init__.py",
    "tests\test_generator.py",
    "tests\test_validator.py",
    "logs\app.log",
    "web\app.py",
    "web\templates\index.html",
    "web\static\style.css"
)

foreach ($file in $files) {
    if (-not (Test-Path $file)) {
        New-Item -ItemType File -Path $file -Force | Out-Null
        Write-Host "   ✅ 파일 생성: $file" -ForegroundColor Green
    } else {
        Write-Host "   ⚠️ 파일 이미 존재: $file" -ForegroundColor Yellow
    }
}

# ============================================================
# 7. data/raw/past_wins.csv 샘플 데이터 생성 (创建示例数据)
# ============================================================
Write-Host ""
Write-Host "📊 4. 샘플 데이터 생성 중... (正在创建示例数据...)" -ForegroundColor Green

$sample_csv = @"
num1,num2,num3,num4,num5,num6
4,8,15,16,23,42
5,12,18,27,35,41
3,7,14,19,28,44
6,11,20,25,33,39
2,9,16,21,34,40
1,10,17,24,32,43
8,13,22,26,31,45
4,9,15,20,30,38
7,14,19,24,29,36
3,11,18,23,28,37
"@

$csvPath = "data\raw\past_wins.csv"
if (-not (Test-Path $csvPath)) {
    $sample_csv | Out-File -FilePath $csvPath -Encoding UTF8
    Write-Host "   ✅ 샘플 데이터 생성: $csvPath" -ForegroundColor Green
} else {
    Write-Host "   ⚠️ 샘플 데이터 이미 존재: $csvPath" -ForegroundColor Yellow
}

# ============================================================
# 8. 완료 메시지 (完成消息)
# ============================================================
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  🎉 프로젝트 생성이 완료되었습니다!" -ForegroundColor Yellow
Write-Host "  🎉 项目创建已完成！" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📁 프로젝트 경로: (Get-Location)" -ForegroundColor White
Write-Host ""
Write-Host "📌 다음 명령어로 구조를 확인하세요:" -ForegroundColor White
Write-Host "   tree /F" -ForegroundColor Gray
Write-Host ""
Write-Host "📌 다음 명령어로 가상 환경을 생성하세요 (선택):" -ForegroundColor White
Write-Host "   python -m venv venv" -ForegroundColor Gray
Write-Host "   venv\Scripts\activate" -ForegroundColor Gray
Write-Host ""
Write-Host "📌 다음 명령어로 필요한 패키지를 설치하세요:" -ForegroundColor White
Write-Host "   pip install -r requirements.txt" -ForegroundColor Gray
Write-Host ""
Write-Host "📌 다음 명령어로 프로그램을 실행하세요:" -ForegroundColor White
Write-Host "   python main.py" -ForegroundColor Gray
Write-Host ""
Write-Host "🍀 행복한 코딩 되세요! (祝您编码愉快！)" -ForegroundColor Magenta

# ============================================================
# 9. (선택) 구조 보기 (可选) 查看结构
# ============================================================
$choice = Read-Host "`n🔍 지금 폴더 구조를 확인하시겠습니까? (y/n) (现在要查看文件夹结构吗？)"
if ($choice -eq 'y' -or $choice -eq 'Y') {
    Write-Host ""
    tree /F
}

# ============================================================
# 10. 스크립트 종료 (脚本结束)
# ============================================================
Write-Host ""
Write-Host "✅ 스크립트가 정상적으로 종료되었습니다. (脚本已正常结束。)" -ForegroundColor Green