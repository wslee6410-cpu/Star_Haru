<#
============================================================
run_dashboard.ps1
행복로또번호 자동 생성기 - 대시보드 실행 스크립트
幸福彩票号码自动生成器 - 仪表板运行脚本

📌 사용 방법 (使用方法):
   PowerShell에서 이 파일이 있는 폴더로 이동한 후 실행
   在PowerShell中移动到本文件所在文件夹后运行
   .\run_dashboard.ps1

📌 기능 (功能):
   1. Flask 웹 서버를 백그라운드에서 실행 (在后台运行Flask Web服务器)
   2. 서버가 준비되면 브라우저로 대시보드 자동 열기 (服务器就绪后自动打开浏览器仪表板)
   3. 서버 종료는 PowerShell 창에서 Ctrl+C (在PowerShell窗口中按Ctrl+C可关闭服务器)
============================================================
#>

# ============================================================
# 1. 스크립트 시작 메시지 (脚本开始消息)
# ============================================================
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  🍀 행복로또번호 자동 생성기 - 대시보드 실행" -ForegroundColor Yellow
Write-Host "  🍀 幸福彩票号码自动生成器 - 仪表板运行" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# ============================================================
# 2. 프로젝트 폴더 경로 설정 (设置项目文件夹路径)
# ============================================================
# 현재 스크립트가 있는 폴더를 프로젝트 루트로 설정
# 将当前脚本所在文件夹设置为项目根目录
$PROJECT_ROOT = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "📂 프로젝트 경로: $PROJECT_ROOT" -ForegroundColor White
Write-Host ""

# ============================================================
# 3. Flask 서버 실행 (Flask服务器运行)
# ============================================================
Write-Host "🚀 1. Flask 서버 실행 중... (正在启动Flask服务器...)" -ForegroundColor Green

# Flask 서버를 백그라운드에서 실행 (在后台运行Flask服务器)
# -NoExit: 실행 후 PowerShell 창을 닫지 않음 (运行后不关闭PowerShell窗口)
# -Command: 실행할 명령어 (要执行的命令)
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PROJECT_ROOT'; python web/app.py"

# ============================================================
# 4. 서버 시작 대기 (等待服务器启动)
# ============================================================
Write-Host ""
Write-Host "⏳ 2. 서버 시작 대기 중... (等待服务器启动...)" -ForegroundColor Yellow

# 서버가 완전히 시작될 때까지 5초 대기 (等待5秒让服务器完全启动)
# 포트 5000번이 열릴 때까지 기다리는 더 정교한 방법도 있지만,
# 初学者을 위해 간단히 5초 대기합니다.
# 也有更精确的等待端口5000打开的方法，但为了初学者，简单等待5秒。
Start-Sleep -Seconds 5

# ============================================================
# 5. 브라우저로 대시보드 열기 (用浏览器打开仪表板)
# ============================================================
Write-Host ""
Write-Host "🌐 3. 브라우저로 대시보드 열기... (用浏览器打开仪表板...)" -ForegroundColor Green

# 대시보드 URL (仪表板URL)
$DASHBOARD_URL = "http://127.0.0.1:5000"

# ============================================================
# 5-1. 기본 브라우저로 열기 (用默认浏览器打开)
# ============================================================
try {
    Start-Process $DASHBOARD_URL
    Write-Host "   ✅ 기본 브라우저로 열기 완료: $DASHBOARD_URL" -ForegroundColor Green
}
catch {
    # 기본 브라우저가 없으면 Chrome이나 Edge로 시도 (如果没有默认浏览器，尝试用Chrome或Edge)
    Write-Host "   ⚠️ 기본 브라우저를 찾을 수 없습니다. Chrome 또는 Edge로 시도합니다." -ForegroundColor Yellow
    
    try {
        Start-Process "chrome" -ArgumentList $DASHBOARD_URL
        Write-Host "   ✅ Chrome으로 열기 완료: $DASHBOARD_URL" -ForegroundColor Green
    }
    catch {
        try {
            Start-Process "msedge" -ArgumentList $DASHBOARD_URL
            Write-Host "   ✅ Edge로 열기 완료: $DASHBOARD_URL" -ForegroundColor Green
        }
        catch {
            Write-Host "   ❌ 브라우저를 자동으로 열 수 없습니다. 직접 브라우저를 열고 주소를 입력하세요." -ForegroundColor Red
            Write-Host "   📌 주소: $DASHBOARD_URL" -ForegroundColor White
        }
    }
}

# ============================================================
# 6. 완료 메시지 (完成消息)
# ============================================================
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  ✅ 대시보드 실행이 완료되었습니다!" -ForegroundColor Yellow
Write-Host "  ✅ 仪表板运行完成！" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📌 대시보드 주소: $DASHBOARD_URL" -ForegroundColor White
Write-Host ""
Write-Host "📌 서버 종료 방법:" -ForegroundColor White
Write-Host "   1. Flask 서버가 실행된 PowerShell 창으로 이동" -ForegroundColor Gray
Write-Host "   2. Ctrl + C 를 누르면 서버가 종료됩니다" -ForegroundColor Gray
Write-Host ""
Write-Host "🍀 즐거운 로또 생성 되세요! (祝您彩票生成愉快！)" -ForegroundColor Magenta

# ============================================================
# 7. 스크립트 종료 (脚本结束)
# ============================================================
Write-Host ""
Write-Host "✅ 스크립트가 정상적으로 종료되었습니다. (脚本已正常结束。)" -ForegroundColor Green