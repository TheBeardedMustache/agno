# install_pdf_tools.ps1 - Install PDF processing dependencies

Write-Host "Installing PDF processing tools..." -ForegroundColor Green

try {
    # Install Python dependencies
    Write-Host "Installing Python packages..." -ForegroundColor Yellow
    pip install PyMuPDF PyPDF2 pdfplumber markdown python-docx beautifulsoup4
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ PDF processing tools installed successfully" -ForegroundColor Green
    } else {
        Write-Host "✗ Some packages may have failed to install" -ForegroundColor Red
    }
    
    # Test the installation
    Write-Host "Testing PDF processing capabilities..." -ForegroundColor Yellow
    $testResult = python -c "import fitz; import PyPDF2; import pdfplumber; print('All PDF tools working!')" 2>&1
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ PDF processing test successful" -ForegroundColor Green
        Write-Host $testResult -ForegroundColor Green
    } else {
        Write-Host "✗ PDF processing test failed" -ForegroundColor Red
        Write-Host $testResult -ForegroundColor Red
    }
    
    Write-Host "`nPDF Processing Features Available:" -ForegroundColor Cyan
    Write-Host "• Convert PDFs to Markdown format" -ForegroundColor White
    Write-Host "• Batch process multiple PDFs" -ForegroundColor White
    Write-Host "• Extract PDF metadata" -ForegroundColor White
    Write-Host "• Organize knowledge base automatically" -ForegroundColor White
    
    Write-Host "`nUsage Examples:" -ForegroundColor Cyan
    Write-Host "python pdf_processor.py convert -i document.pdf -o document.md" -ForegroundColor White
    Write-Host "python pdf_processor.py batch -i ./pdfs/ -o ./markdown/" -ForegroundColor White
    Write-Host "python pdf_processor.py metadata -i document.pdf" -ForegroundColor White
    
} catch {
    Write-Host "Error installing PDF tools: $($_.Exception.Message)" -ForegroundColor Red
}