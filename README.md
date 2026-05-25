
<!DOCTYPE html>
<html lang="fr" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bit Wise - La Banque Digitale</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<style>
:root {
--primary: #0a0f1d; --primary-light: #1e293b; --secondary: #3b82f6; --secondary-dark: #2563eb;
--accent: #10b981; --accent-hover: #059669; --danger: #ef4444; --warning: #f59e0b;
--bg-body: #f8fafc; --bg-card: #ffffff; --bg-glass: rgba(255, 255, 255, 0.85);
--border: #e2e8f0; --border-focus: #3b82f6; --text-primary: #0f172a; --text-secondary: #475569;
--text-muted: #94a3b8; --text-white: #ffffff;
--shadow-sm: 0 1px 2px rgba(0,0,0,0.04); --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
--shadow-lg: 0 8px 30px rgba(0,0,0,0.12); --blur-glass: blur(12px);
--transition-fast: 150ms ease; --transition-normal: 250ms cubic-bezier(0.4, 0, 0.2, 1);
--radius-sm: 8px; --radius-md: 12px; --radius-lg: 16px; --radius-xl: 24px; --radius-full: 9999px;
--chart-grid: rgba(0,0,0,0.06); --chart-text: #64748b;
}
[data-theme="dark"] {
--bg-body: #0b1120; --bg-card: #1e293b; --bg-glass: rgba(30, 41, 59, 0.85);
--border: #334155; --text-primary: #f8fafc; --text-secondary: #cbd5e1; --text-muted: #64748b;
--shadow-sm: 0 1px 2px rgba(0,0,0,0.4); --shadow-md: 0 4px 12px rgba(0,0,0,0.5); --shadow-lg: 0 8px 30px rgba(0,0,0,0.6);
--chart-grid: rgba(255,255,255,0.1); --chart-text: #94a3b8;
}
[data-theme="dark"] input, [data-theme="dark"] select, [data-theme="dark"] textarea { background: #0f172a; color: var(--text-primary); }
[data-theme="dark"] .balance-amount { background: linear-gradient(135deg, #f8fafc, #94a3b8); -webkit-background-clip: text; }
[data-theme="dark"] .result-card.highlight { background: linear-gradient(135deg, #1e3a5f, #0f172a); border-color: var(--secondary); }
[data-theme="dark"] .toast { background: #1e293b; border: 1px solid var(--border); }
[data-theme="dark"] .modal-content { background: #1e293b; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', sans-serif; background: var(--bg-body); color: var(--text-primary); line-height: 1.6; -webkit-font-smoothing: antialiased; transition: background 0.4s ease, color 0.4s ease; }
h1, h2, h3, h4 { font-weight: 600; line-height: 1.3; color: var(--text-primary); letter-spacing: -0.02em; }
h1 { font-size: 2.5rem; } h2 { font-size: 1.75rem; } h3 { font-size: 1.25rem; }
p { color: var(--text-secondary); }
header { background: linear-gradient(135deg, var(--primary), var(--primary-light)); color: var(--text-white); padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; box-shadow: var(--shadow-lg); backdrop-filter: var(--blur-glass); }
.header-left { display: flex; align-items: center; gap: 20px; }
.logo { font-size: 1.5rem; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 8px; }
.logo i { color: var(--secondary); }
.logo span { background: linear-gradient(135deg, var(--secondary), var(--accent)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.nav-container { display: flex; align-items: center; gap: 24px; }
.nav-container ul { list-style: none; display: flex; flex-direction: row; flex-wrap: nowrap; align-items: center; gap: 24px; margin: 0; padding: 0; }
.nav-container li { list-style: none; }
.nav-container a { color: rgba(255,255,255,0.85); text-decoration: none; font-weight: 500; font-size: 0.95rem; cursor: pointer; transition: var(--transition-fast); padding: 8px 4px; position: relative; white-space: nowrap; display: inline-block; }
.nav-container a:hover, .nav-container a.active { color: var(--text-white); }
.nav-container a::after { content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--secondary); transition: var(--transition-normal); border-radius: var(--radius-full); }
.nav-container a:hover::after, .nav-container a.active::after { width: 100%; }
.hamburger { display: none; background: none; border: none; color: white; font-size: 1.5rem; cursor: pointer; }
.mobile-menu { position: fixed; top: 70px; right: -100%; width: 80%; max-width: 300px; height: calc(100vh - 70px); background: var(--primary-light); padding: 20px; transition: right 0.3s ease; z-index: 999; box-shadow: var(--shadow-lg); }
.mobile-menu.open { right: 0; }
.mobile-menu ul { list-style: none; display: flex; flex-direction: column; gap: 15px; }
.mobile-menu a { display: block; padding: 10px; color: white; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.1); }
.auth-buttons { display: flex; gap: 8px; align-items: center; }
.auth-buttons button { padding: 8px 14px; border-radius: var(--radius-md); border: none; cursor: pointer; font-weight: 600; font-size: 0.8rem; transition: var(--transition-normal); }
.btn-login { background: transparent; color: var(--text-white); border: 1px solid rgba(255,255,255,0.3); }
.btn-login:hover { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.5); }
.btn-register { padding: 5px 10px; font-size: 0.75rem; line-height: 1.2; background: linear-gradient(135deg, var(--secondary), var(--secondary-dark)); color: var(--text-white); box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4); }
.btn-register:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6); }
.btn-theme { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; width: 40px; height: 40px; border-radius: var(--radius-full); display: flex; align-items: center; justify-content: center; cursor: pointer; transition: var(--transition-fast); }
.btn-theme:hover { background: rgba(255,255,255,0.2); transform: rotate(15deg); }
#lang-selector { background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 6px 10px; border-radius: var(--radius-full); cursor: pointer; font-size: 0.85rem; outline: none; max-width: 180px; }
#lang-selector option { background: var(--bg-card); color: var(--text-primary); padding: 6px; }
main { min-height: 80vh; max-width: 1200px; margin: 0 auto; padding: 48px 24px; }
.page-section { display: none; animation: fadeInUp 0.5s var(--transition-normal); }
.page-section.active { display: block; }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: translateY(0); } }
.scroll-animate { opacity: 0; transform: translateY(30px); transition: opacity 0.6s ease, transform 0.6s ease; }
.scroll-animate.visible { opacity: 1; transform: translateY(0); }
.card { background: var(--bg-card); padding: 32px; border-radius: var(--radius-lg); box-shadow: var(--shadow-md); margin-bottom: 24px; border: 1px solid var(--border); transition: var(--transition-normal); }
.card:hover { box-shadow: var(--shadow-lg); transform: translateY(-2px); }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; }
.grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }
.btn { padding: 12px 24px; border: none; border-radius: var(--radius-md); cursor: pointer; font-weight: 600; font-size: 0.95rem; transition: var(--transition-normal); display: inline-flex; align-items: center; justify-content: center; gap: 8px; text-decoration: none; position: relative; overflow: hidden; }
.btn::after { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(180deg, rgba(255,255,255,0.15), transparent); opacity: 0; transition: var(--transition-fast); }
.btn:hover::after { opacity: 1; } .btn:active { transform: translateY(1px); }
.btn-primary { background: linear-gradient(135deg, var(--secondary), var(--secondary-dark)); color: white; box-shadow: 0 4px 14px rgba(59, 130, 246, 0.35); }
.btn-primary:hover { box-shadow: 0 6px 20px rgba(59, 130, 246, 0.55); transform: translateY(-2px); }
.btn-success { background: linear-gradient(135deg, var(--accent), var(--accent-hover)); color: white; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35); }
.btn-success:hover { box-shadow: 0 6px 20px rgba(16, 185, 129, 0.55); transform: translateY(-2px); }
.btn-danger { background: linear-gradient(135deg, var(--danger), #dc2626); color: white; }
.btn-danger:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); }
.btn-dark { background: var(--primary-light); color: white; }
.btn-dark:hover { background: var(--primary); transform: translateY(-2px); }
.btn-instant { background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: white; }
.btn-crypto { background: linear-gradient(135deg, #f7931a, #eab308); color: white; }
.btn:disabled { opacity: 0.6; cursor: not-allowed; transform: none !important; box-shadow: none !important; }
input, select, textarea { width: 100%; padding: 14px 16px; margin: 8px 0; border: 1px solid var(--border); border-radius: var(--radius-md); box-sizing: border-box; font-size: 1rem; transition: var(--transition-fast); background: var(--bg-card); color: var(--text-primary); }
input:focus, select:focus, textarea:focus { outline: none; border-color: var(--border-focus); box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.12); }
.phone-group { display: flex; gap: 12px; } .phone-group select { width: 35%; } .phone-group input { width: 65%; }
label { display: block; font-weight: 500; color: var(--text-primary); margin-bottom: 6px; font-size: 0.9rem; }
.balance-card { background: linear-gradient(135deg, var(--primary), var(--primary-light)); color: white; text-align: center; border: none; box-shadow: 0 12px 40px rgba(10, 15, 29, 0.3); }
.balance-card h3 { color: rgba(255,255,255,0.9); font-weight: 500; }
.balance-amount { font-size: 3rem; font-weight: 700; margin: 12px 0; background: linear-gradient(135deg, #fff, #cbd5e1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.iban-display { font-family: monospace; background: rgba(255,255,255,0.12); padding: 8px 16px; border-radius: var(--radius-md); display: inline-block; margin-top: 8px; font-size: 0.95rem; letter-spacing: 1px; }
.transaction-list { max-height: 320px; overflow-y: auto; }
.t-item { display: flex; justify-content: space-between; padding: 14px 16px; border-bottom: 1px solid var(--border); transition: var(--transition-fast); border-radius: var(--radius-sm); }
.t-item:hover { background: var(--bg-body); }
.t-plus { color: var(--accent); font-weight: 600; } .t-minus { color: var(--danger); font-weight: 600; }
.visa-real { background: linear-gradient(135deg, #1e3a5f, #0f172a, #1e293b); color: white; width: 100%; max-width: 360px; height: 220px; border-radius: var(--radius-lg); padding: 24px; margin: 0 auto; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 20px 50px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1); position: relative; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); }
.chip { width: 50px; height: 40px; background: linear-gradient(135deg, #fbbf24, #f59e0b); border-radius: 6px; border: 1px solid #d97706; }
.card-holder-name { text-transform: uppercase; letter-spacing: 2px; font-weight: 600; font-size: 1rem; color: rgba(255,255,255,0.95); }
.dashboard-clock-container { background: var(--bg-glass); padding: 12px 24px; border-radius: var(--radius-full); box-shadow: var(--shadow-sm); display: inline-flex; align-items: center; gap: 12px; margin-bottom: 28px; border: 1px solid var(--border); backdrop-filter: var(--blur-glass); }
.clock-time { font-family: monospace; font-weight: 700; font-size: 1.3rem; color: var(--text-primary); }
.clock-date { color: var(--text-muted); font-size: 0.9rem; }
footer { background: linear-gradient(180deg, var(--primary-light), var(--primary)); color: var(--text-muted); padding: 72px 24px 32px; margin-top: 80px; font-size: 0.9rem; }
.footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 48px; max-width: 1200px; margin: 0 auto 48px; }
.footer-col h4 { color: var(--text-white); margin-bottom: 20px; font-size: 1rem; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600; }
.footer-col ul { list-style: none; padding: 0; }
.footer-col li { margin-bottom: 14px; cursor: pointer; transition: var(--transition-fast); color: var(--text-muted); }
.footer-col li:hover { color: var(--secondary); transform: translateX(4px); }
.legal-bar { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 32px; text-align: center; max-width: 1200px; margin: 0 auto; font-size: 0.85rem; line-height: 1.8; color: var(--text-muted); }
.legal-bar p { margin: 0 0 8px; }
.legal-bar .legal-links { margin-top: 16px; }
.legal-bar .legal-links a { color: var(--text-muted); cursor: pointer; transition: var(--transition-fast); }
.legal-bar .legal-links a:hover { color: var(--secondary); }
.floating-icons > div, .floating-icons > a { position: fixed; bottom: 24px; width: 56px; height: 56px; border-radius: var(--radius-full); display: flex; align-items: center; justify-content: center; color: white; font-size: 22px; box-shadow: var(--shadow-lg); cursor: pointer; z-index: 2000; transition: var(--transition-normal); border: 2px solid rgba(255,255,255,0.2); text-decoration: none; }
.floating-icons > div:hover, .floating-icons > a:hover { transform: translateY(-4px) scale(1.05); }
.wa-icon { right: 24px; background: linear-gradient(135deg, #25D366, #128C7E); }
.mail-icon { left: 24px; background: linear-gradient(135deg, #EA4335, #c5221f); }
#back-to-top { position: fixed; bottom: 90px; right: 24px; width: 50px; height: 50px; background: var(--secondary); color: white; border-radius: var(--radius-full); display: flex; align-items: center; justify-content: center; cursor: pointer; opacity: 0; pointer-events: none; transition: all 0.3s ease; z-index: 1999; box-shadow: var(--shadow-lg); transform: translateY(20px); }
#back-to-top.visible { opacity: 1; pointer-events: all; transform: translateY(0); }
.modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(10, 15, 29, 0.75); justify-content: center; align-items: center; z-index: 3000; backdrop-filter: blur(8px); animation: fadeIn 0.2s ease; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
.modal-content { background: var(--bg-card); padding: 36px; border-radius: var(--radius-xl); width: 520px; max-width: 92%; text-align: left; box-shadow: var(--shadow-lg); max-height: 90vh; overflow-y: auto; border: 1px solid var(--border); animation: slideUp 0.3s var(--transition-normal); }
@keyframes slideUp { from { opacity: 0; transform: translateY(20px) scale(0.98); } to { opacity: 1; transform: translateY(0) scale(1); } }
.toast-container { position: fixed; top: 24px; right: 24px; z-index: 9999; display: flex; flex-direction: column; gap: 12px; pointer-events: none; }
.toast { background: var(--bg-card); padding: 16px 20px; border-radius: var(--radius-md); box-shadow: var(--shadow-lg); display: flex; align-items: flex-start; gap: 14px; min-width: 340px; pointer-events: auto; animation: toastSlide 0.3s var(--transition-normal); border-left: 4px solid var(--secondary); border: 1px solid var(--border); }
@keyframes toastSlide { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
.toast.success { border-left-color: var(--accent); } .toast.warning { border-left-color: var(--warning); } .toast.error { border-left-color: var(--danger); }
.toast-icon { font-size: 1.4rem; color: var(--text-muted); margin-top: 2px; }
.toast.success .toast-icon { color: var(--accent); } .toast.warning .toast-icon { color: var(--warning); } .toast.error .toast-icon { color: var(--danger); }
.toast-content { flex: 1; } .toast-title { font-weight: 600; margin-bottom: 4px; font-size: 1rem; color: var(--text-primary); }
.toast-message { font-size: 0.9rem; color: var(--text-secondary); line-height: 1.4; }
.toast-close { cursor: pointer; color: var(--text-muted); font-size: 1.2rem; transition: var(--transition-fast); padding: 4px; border-radius: var(--radius-sm); }
.credit-header { margin-bottom: 32px; } .credit-subtitle { color: var(--text-muted); margin: 8px 0 0 0; font-size: 1.05rem; }
.credit-card { border: 1px solid var(--border); border-radius: var(--radius-lg); box-shadow: var(--shadow-md); margin-bottom: 24px; background: var(--bg-card); }
.section-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; border-bottom: 1px solid var(--border); padding-bottom: 16px; }
.section-header h3 { display: flex; align-items: center; gap: 10px; }
.badge { padding: 6px 14px; border-radius: var(--radius-full); font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.badge.pending { background: #fef3c7; color: #92400e; } .badge.approved { background: #dcfce7; color: #166534; } .badge.rejected { background: #fee2e2; color: #991b1b; }
.scoring-grid { display: grid; grid-template-columns: 1fr 2fr; gap: 28px; align-items: center; }
.score-display { text-align: center; }
.score-circle { width: 100px; height: 100px; border-radius: 50%; border: 4px solid var(--border); display: flex; flex-direction: column; justify-content: center; align-items: center; margin: 0 auto 16px; background: var(--bg-card); }
.score-circle.good { border-color: var(--accent); color: var(--accent); } .score-circle.fair { border-color: var(--warning); color: var(--warning); } .score-circle.poor { border-color: var(--danger); color: var(--danger); }
#score-value { font-size: 2rem; font-weight: 700; } .score-circle small { font-size: 0.75rem; color: var(--text-muted); }
.info-row { display: flex; align-items: flex-start; gap: 14px; margin-bottom: 14px; padding: 12px; background: var(--bg-body); border-radius: var(--radius-md); }
.info-row i { color: var(--secondary); width: 20px; font-size: 1.1rem; margin-top: 3px; }
.simulator-results { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 24px 0; }
.result-card { background: var(--bg-body); padding: 20px; border-radius: var(--radius-md); text-align: center; border: 1px solid var(--border); transition: var(--transition-fast); }
.result-card:hover { border-color: var(--secondary); }
.result-card small { color: var(--text-muted); display: block; margin-bottom: 8px; font-size: 0.85rem; }
.result-card strong { font-size: 1.4rem; color: var(--text-primary); font-weight: 700; }
.result-card.highlight { background: linear-gradient(135deg, #eff6ff, #dbeafe); border: 2px solid var(--secondary); position: relative; }
.result-card.highlight::before { content: 'Recommandé'; position: absolute; top: -10px; right: 16px; background: var(--secondary); color: white; font-size: 0.7rem; padding: 4px 10px; border-radius: var(--radius-full); font-weight: 600; }
.debt-ratio-container { background: var(--bg-body); padding: 20px; border-radius: var(--radius-md); margin-bottom: 24px; border: 1px solid var(--border); }
.ratio-header { display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.9rem; font-weight: 500; }
.ratio-bar { height: 10px; background: var(--border); border-radius: var(--radius-full); overflow: hidden; }
.ratio-fill { height: 100%; border-radius: var(--radius-full); transition: width 0.5s ease, background 0.3s; }
.ratio-fill.warning { background: var(--warning); } .ratio-fill.danger { background: var(--danger); }
.ratio-status { margin-top: 12px; font-size: 0.9rem; font-weight: 600; display: flex; align-items: center; gap: 6px; }
.calendar-section .info-text { font-size: 0.9rem; color: var(--text-muted); margin: 8px 0 20px; display: flex; align-items: center; gap: 8px; }
.table-wrapper { max-height: 280px; overflow-y: auto; border: 1px solid var(--border); border-radius: var(--radius-md); background: var(--bg-card); }
.credit-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.credit-table th { background: var(--bg-body); position: sticky; top: 0; padding: 14px 16px; text-align: left; font-weight: 600; color: var(--text-primary); border-bottom: 2px solid var(--border); }
.credit-table td { padding: 14px 16px; border-bottom: 1px solid var(--border); color: var(--text-secondary); }
.credit-table tr:hover { background: var(--bg-body); }
.timeline { display: flex; justify-content: space-between; margin: 36px 0 24px; position: relative; }
.timeline::before { content: ''; position: absolute; top: 18px; left: 8%; right: 8%; height: 3px; background: var(--border); z-index: 0; border-radius: var(--radius-full); }
.timeline .step { position: relative; z-index: 1; text-align: center; background: var(--bg-card); padding: 0 8px; flex: 1; }
.timeline .step i { display: block; width: 36px; height: 36px; background: var(--border); border-radius: 50%; line-height: 36px; margin: 0 auto 10px; color: var(--text-muted); font-size: 0.9rem; transition: var(--transition-normal); }
.timeline .step.active i { background: var(--secondary); color: white; }
.timeline .step span { font-size: 0.8rem; color: var(--text-muted); font-weight: 500; }
.progress-modern { display: flex; align-items: center; gap: 16px; margin: 24px 0; }
.progress-track { flex: 1; height: 8px; background: var(--border); border-radius: var(--radius-full); overflow: hidden; }
.progress-fill { height: 100%; background: linear-gradient(90deg, var(--secondary), var(--accent)); transition: width 0.5s ease; border-radius: var(--radius-full); }
.status-text { text-align: center; color: var(--text-secondary); font-weight: 500; min-width: 60px; }
.info-banner { padding: 14px 18px; border-radius: var(--radius-md); margin: 20px 0; display: flex; align-items: center; gap: 12px; font-size: 0.9rem; border: 1px solid; }
.info-banner.warning { background: #fffbeb; border-color: #fcd34d; color: #92400e; }
.info-banner.warning i { color: var(--warning); }
.success-header { text-align: center; margin-bottom: 24px; }
.success-header i { font-size: 3.5rem; color: var(--accent); margin-bottom: 16px; animation: bounce 0.6s ease; }
@keyframes bounce { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }
.amount-display { text-align: center; background: linear-gradient(135deg, #dcfce7, #bbf7d0); padding: 24px; border-radius: var(--radius-lg); margin: 20px 0; border: 2px solid var(--accent); }
.amount-display small { color: #166534; display: block; font-weight: 500; margin-bottom: 8px; }
.amount-display div { font-size: 2.2rem; font-weight: 700; color: #064e3b; }
.transfer-box { display: flex; align-items: center; justify-content: center; gap: 24px; background: linear-gradient(135deg, #eff6ff, #dbeafe); padding: 24px; border-radius: var(--radius-lg); margin: 20px 0; border: 2px dashed var(--secondary); }
.transfer-arrow i { font-size: 1.8rem; color: var(--secondary); animation: pulse 2s infinite; }
@keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.7; transform: scale(0.95); } }
.transfer-details { text-align: left; } .transfer-details p { margin: 0; color: var(--text-muted); font-size: 0.9rem; font-weight: 500; }
.transfer-details strong { font-size: 2rem; color: var(--text-primary); font-weight: 700; }
.history-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 24px; margin-top: 24px; box-shadow: var(--shadow-sm); }
.history-card h4 { margin: 0 0 20px 0; display: flex; justify-content: space-between; align-items: center; font-size: 1.1rem; }
.btn-export { background: linear-gradient(135deg, #ef4444, #dc2626); color: white; border: none; padding: 10px 18px; border-radius: var(--radius-md); cursor: pointer; font-size: 0.9rem; display: flex; align-items: center; gap: 8px; transition: var(--transition-normal); font-weight: 500; }
.status-badge { padding: 4px 12px; border-radius: var(--radius-full); font-size: 0.75rem; font-weight: 600; text-transform: capitalize; }
.badge-completed { background: #dcfce7; color: #166534; } .badge-analyzing { background: #e0f2fe; color: #0369a1; } .badge-approved { background: #fef3c7; color: #b45309; } .badge-cancelled { background: #fee2e2; color: #991b1b; } .badge-contract_signed { background: #ede9fe; color: #6d28d9; }
.support-option { display: flex; align-items: center; padding: 16px 20px; border: 1px solid var(--border); border-radius: var(--radius-md); margin-bottom: 12px; text-decoration: none; color: var(--text-primary); transition: var(--transition-normal); background: var(--bg-card); cursor: pointer; }
.support-option:hover { background: linear-gradient(135deg, #f8fafc, #f1f5f9); border-color: var(--secondary); transform: translateX(4px); }
.support-icon { font-size: 1.4rem; margin-right: 16px; width: 30px; text-align: center; color: var(--secondary); }
.ai-chat-header { display: flex; justify-content: space-between; align-items: center; padding: 18px 20px; border-bottom: 1px solid var(--border); background: linear-gradient(135deg, var(--primary), var(--primary-light)); border-radius: var(--radius-xl) var(--radius-xl) 0 0; color: var(--text-white); }
.ai-chat-title { display: flex; align-items: center; gap: 12px; color: var(--text-white); }
.ai-chat-title strong { color: var(--text-white); font-size: 1rem; }
.ai-chat-title > div > div { color: rgba(255,255,255,0.8) !important; }
.ai-chat-avatar { width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, var(--secondary), var(--accent)); display: flex; align-items: center; justify-content: center; color: white; font-size: 1.1rem; }
.ai-status-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--accent); animation: pulse 2s infinite; display: inline-block; }
.ai-chat-close { background: rgba(255,255,255,0.1); border: none; color: white; width: 34px; height: 34px; border-radius: 50%; cursor: pointer; transition: var(--transition-fast); display: flex; align-items: center; justify-content: center; }
.ai-chat-close:hover { background: rgba(255,255,255,0.25); }
.ai-chat-body { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 12px; background: var(--bg-body); }
.ai-msg { max-width: 85%; padding: 10px 14px; border-radius: var(--radius-md); font-size: 0.92rem; line-height: 1.45; word-wrap: break-word; white-space: pre-wrap; }
.ai-msg.bot { align-self: flex-start; background: var(--bg-card); border: 1px solid var(--border); border-bottom-left-radius: 4px; color: var(--text-primary); }
.ai-msg.user { align-self: flex-end; background: linear-gradient(135deg, var(--secondary), #2563eb); color: white; border-bottom-right-radius: 4px; }
.ai-msg.typing { display: inline-flex; gap: 4px; align-items: center; }
.ai-msg.typing span { width: 6px; height: 6px; border-radius: 50%; background: var(--text-muted); animation: typingDot 1.4s infinite; }
.ai-msg.typing span:nth-child(2) { animation-delay: 0.2s; }
.ai-msg.typing span:nth-child(3) { animation-delay: 0.4s; }
@keyframes typingDot { 0%, 60%, 100% { transform: translateY(0); opacity: 0.4; } 30% { transform: translateY(-4px); opacity: 1; } }
.ai-chat-input-bar { display: flex; gap: 8px; padding: 14px; border-top: 1px solid var(--border); background: var(--bg-card); border-radius: 0 0 var(--radius-xl) var(--radius-xl); }
.ai-chat-input-bar input { flex: 1; padding: 10px 14px; border: 1px solid var(--border); border-radius: var(--radius-full); background: var(--bg-body); color: var(--text-primary); font-size: 0.95rem; outline: none; transition: var(--transition-fast); }
.ai-chat-input-bar input:focus { border-color: var(--secondary); }
.ai-chat-send { width: 42px; height: 42px; border-radius: 50%; border: none; background: linear-gradient(135deg, var(--secondary), #2563eb); color: white; cursor: pointer; transition: var(--transition-normal); display: flex; align-items: center; justify-content: center; }
.ai-chat-send:hover { transform: scale(1.05); box-shadow: var(--shadow-md); }
.ai-chat-send:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
#loading-screen { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: var(--primary); z-index: 10000; display: flex; flex-direction: column; align-items: center; justify-content: center; transition: opacity 0.5s ease, visibility 0.5s ease; }
#loading-screen.hidden { opacity: 0; visibility: hidden; pointer-events: none; }
.loader { width: 48px; height: 48px; border: 4px solid rgba(255,255,255,0.2); border-top: 4px solid var(--secondary); border-radius: 50%; animation: spin 1s linear infinite; margin-bottom: 16px; }
@keyframes spin { 100% { transform: rotate(360deg); } }
.loader-text { color: white; font-size: 1.1rem; font-weight: 500; letter-spacing: 1px; }
.chart-card { position: relative; }
.chart-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px; }
.chart-title { font-size: 1.1rem; font-weight: 600; display: flex; align-items: center; gap: 8px; }
.chart-filters { display: flex; gap: 8px; background: var(--bg-body); padding: 4px; border-radius: var(--radius-md); }
.chart-filter { padding: 6px 14px; border: none; background: transparent; border-radius: var(--radius-sm); cursor: pointer; font-size: 0.85rem; font-weight: 500; color: var(--text-secondary); transition: var(--transition-fast); }
.chart-filter.active, .chart-filter:hover { background: var(--secondary); color: white; }
.chart-container { position: relative; height: 280px; width: 100%; }
.chart-legend { display: flex; justify-content: center; gap: 24px; margin-top: 16px; font-size: 0.85rem; color: var(--text-muted); }
.legend-item { display: flex; align-items: center; gap: 6px; } .legend-dot { width: 12px; height: 12px; border-radius: 50%; }
.legend-dot.income { background: var(--accent); } .legend-dot.expense { background: var(--danger); }
.chart-actions { display: flex; gap: 8px; margin-top: 12px; }
.btn-chart-export { padding: 6px 12px; font-size: 0.8rem; background: var(--bg-body); border: 1px solid var(--border); border-radius: var(--radius-sm); cursor: pointer; color: var(--text-secondary); display: flex; align-items: center; gap: 6px; transition: var(--transition-fast); }
.btn-chart-export:hover { background: var(--secondary); color: white; border-color: var(--secondary); }
.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 12px; margin-top: 16px; }
.stat-card { background: var(--bg-body); padding: 12px 16px; border-radius: var(--radius-md); text-align: center; }
.stat-card .value { font-size: 1.3rem; font-weight: 700; color: var(--text-primary); }
.stat-card .label { font-size: 0.8rem; color: var(--text-muted); margin-top: 4px; }
.api-status { display: flex; align-items: center; gap: 8px; font-size: 0.85rem; color: var(--text-muted); padding: 8px 12px; background: var(--bg-body); border-radius: var(--radius-sm); margin-top: 12px; }
.api-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--accent); animation: pulse 2s infinite; }
/* === MISES A JOUR AJOUTÉES (Non destructives) === */
.goal-card { transition: var(--transition-normal); border: 1px solid var(--border); position: relative; overflow: hidden; padding: 16px; text-align: center; }
.goal-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: var(--goal-gradient, var(--secondary)); }
.goal-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); border-color: var(--secondary); }
.goal-icon-wrapper { width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin: 0 auto 10px; background: var(--goal-gradient); color: white; box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
.goal-progress-bar { height: 8px; border-radius: 4px; background: var(--border); overflow: hidden; margin: 8px 0; }
.goal-progress-fill { height: 100%; border-radius: 4px; background: var(--goal-gradient); transition: width 0.5s ease; }
.goal-actions { display: flex; gap: 8px; margin-top: 12px; } .goal-actions .btn { flex: 1; padding: 8px; font-size: 0.85rem; }
.goal-reached-badge { position: absolute; top: 10px; right: 10px; background: var(--accent); color: white; padding: 3px 8px; border-radius: 20px; font-size: 0.7rem; font-weight: 600; animation: pulse 2s infinite; }
[data-theme="dark"] .goal-card { background: linear-gradient(145deg, #1e293b, #0f172a); }
.crypto-asset-row { display:flex; align-items:center; gap:10px; padding:8px 0; border-bottom:1px solid var(--border); }
.crypto-asset-row:last-child { border-bottom:none; }
.crypto-icon { width:32px; height:32px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:var(--bg-body); font-weight:bold; font-size:0.8rem; color:var(--text-secondary); }
.crypto-name { flex:1; font-weight:500; } .crypto-price { font-weight:600; font-family:monospace; }
.crypto-change { font-weight:600; min-width:60px; text-align:right; } .crypto-change.positive { color:var(--accent); } .crypto-change.negative { color:var(--danger); }
.watchlist-card { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius-md); padding:16px; transition:var(--transition-normal); position:relative; margin-bottom:8px; }
.watchlist-card:hover { transform:translateY(-2px); box-shadow:var(--shadow-md); border-color:var(--secondary); }
.watchlist-remove { position:absolute; top:8px; right:8px; background:none; border:none; color:var(--text-muted); cursor:pointer; } .watchlist-remove:hover { color:var(--danger); }
.ob-row { display:flex; justify-content:space-between; padding:2px 4px; position:relative; transition:background 0.2s; } .ob-row:hover { background:var(--bg-card); }
.ob-bid { color:var(--accent); } .ob-ask { color:var(--danger); } .ob-bar { position:absolute; right:0; top:0; height:100%; opacity:0.12; z-index:0; }
.ob-spread { text-align:center; padding:6px; background:var(--bg-card); border-radius:6px; margin:2px 0; font-weight:700; font-size:0.95rem; border:1px solid var(--border); }
.signal-badge { padding: 4px 10px; border-radius: var(--radius-full); font-size: 0.75rem; font-weight: 700; text-transform: uppercase; }
.signal-buy { background: #dcfce7; color: #166534; } .signal-sell { background: #fee2e2; color: #991b1b; } .signal-hold { background: #fef3c7; color: #92400e; }
.rsi-container { display: flex; align-items: center; gap: 8px; font-size: 0.85rem; } .rsi-bar { flex: 1; height: 6px; background: var(--border); border-radius: 3px; overflow: hidden; }
.rsi-fill { height: 100%; transition: width 0.3s, background 0.3s; } .rsi-fill.oversold { background: var(--accent); } .rsi-fill.neutral { background: var(--warning); } .rsi-fill.overbought { background: var(--danger); }
.dca-plan { display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; background: var(--bg-body); border-radius: var(--radius-md); margin-bottom: 8px; border-left: 4px solid var(--accent); }
.dca-plan .info { flex: 1; } .dca-plan .info strong { display: block; margin-bottom: 4px; } .dca-plan .meta { font-size: 0.8rem; color: var(--text-muted); }
.dca-plan .actions button { padding: 6px 10px; font-size: 0.8rem; margin-left: 6px; }
.fee-result-row { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid var(--border); font-size: 0.9rem; } .fee-result-row:last-child { border-bottom: none; }
.ws-dot { width:8px;height:8px;border-radius:50%;background:var(--text-muted); transition: all 0.3s ease; } .ws-dot.connected { background: var(--accent); box-shadow: 0 0 0 2px rgba(16,185,129,0.2); }
.ws-dot.disconnected { background: var(--danger); } .ws-dot.connecting { background: var(--warning); animation: pulse 1.5s infinite; }
.glass-widget { position:fixed; bottom:100px; left:24px; z-index:1998; background:var(--bg-glass); backdrop-filter:var(--blur-glass); border:1px solid var(--border); border-radius:var(--radius-lg); box-shadow:var(--shadow-lg); overflow:hidden; width:220px; transition:all 0.3s cubic-bezier(0.4,0,0.2,1); user-select:none; }
.glass-widget .widget-header { padding:12px 16px; cursor:pointer; display:flex; align-items:center; background:linear-gradient(135deg, rgba(59,130,246,0.1), transparent); }
.glass-widget .widget-body { max-height:0; overflow:hidden; transition:max-height 0.3s ease, padding 0.3s; background:var(--bg-card); padding:0 16px; }
.glass-widget.expanded .widget-body { max-height:160px; padding:8px 16px 12px; } .glass-widget.expanded #float-arrow { transform:rotate(180deg); }
.float-item { display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid var(--border); font-size:0.9rem; } .float-item:last-child { border-bottom:none; padding-bottom:0; }
.pnl-positive { color: var(--accent) !important; } .pnl-negative { color: var(--danger) !important; }
.account-card { background:var(--bg-body); border:2px solid var(--border); border-radius:var(--radius-md); padding:16px; cursor:pointer; transition:0.3s; position:relative; }
.account-card:hover { border-color:var(--secondary); transform:translateY(-2px); box-shadow:var(--shadow-md); }
.account-card.active { border-color:var(--accent); background:linear-gradient(135deg, rgba(16,185,129,0.12), transparent); box-shadow:0 0 0 2px rgba(16,185,129,0.3); }
.account-card .bal { font-size:1.3rem; font-weight:700; margin:6px 0; } .account-card .perf { font-size:0.85rem; } .perf.positive { color:var(--accent); } .perf.negative { color:var(--danger); }
.order-badge { padding:3px 8px; border-radius:4px; font-size:0.75rem; font-weight:600; }
.order-open { background:var(--warning); color:#000; } .order-filled { background:var(--accent); color:#fff; } .order-cancelled { background:var(--danger); color:#fff; }
[data-theme="dark"] .ob-bar { opacity:0.18; } [data-theme="dark"] .signal-buy { background: rgba(22, 101, 52, 0.3); color: #86efac; }
[data-theme="dark"] .signal-sell { background: rgba(153, 27, 27, 0.3); color: #fca5a5; } [data-theme="dark"] .signal-hold { background: rgba(146, 64, 14, 0.3); color: #fde047; }
.bt-stat-card { text-align:center; padding:12px; background:var(--bg-body); border-radius:var(--radius-md); } .bt-stat-card .val { font-size:1.2rem; font-weight:700; color:var(--text-primary); } .bt-stat-card .lbl { font-size:0.8rem; color:var(--text-muted); margin-top:4px; }
.history-type-buy_dca { color: var(--accent); font-weight: 600; }
/* --- Dropdown & FAQ Styles --- */
.nav-container .dropdown { position: relative; }
.nav-container .dropdown-menu {
display: none; position: absolute; top: calc(100% + 8px); left: 0;
background: var(--primary-light); min-width: 210px; border-radius: var(--radius-md);
box-shadow: var(--shadow-lg); padding: 8px 0; z-index: 1001; list-style: none;
border: 1px solid rgba(255,255,255,0.1); opacity: 0; transform: translateY(10px); transition: all 0.2s ease;
}
.nav-container .dropdown:hover .dropdown-menu { display: block; opacity: 1; transform: translateY(0); }
.nav-container .dropdown-menu li a {
display: block; padding: 12px 20px; color: rgba(255,255,255,0.85);
text-decoration: none; font-size: 0.9rem; transition: var(--transition-fast); white-space: nowrap;
}
.nav-container .dropdown-menu li a:hover { background: rgba(255,255,255,0.1); color: var(--text-white); }
.nav-container .dropdown-menu li a::after { display: none; }
.faq-item { border-bottom: 1px solid var(--border); padding: 18px 0; cursor: pointer; }
.faq-item:last-child { border-bottom: none; }
.faq-item h3 { margin: 0; display: flex; justify-content: space-between; align-items: center; font-size: 1.1rem; transition: color 0.2s; }
.faq-item h3:hover { color: var(--secondary); }
.faq-item p { max-height: 0; overflow: hidden; transition: max-height 0.35s ease, padding 0.35s ease; margin-top: 0; color: var(--text-secondary); }
.faq-item.open p { max-height: 300px; padding-top: 14px; }
.faq-item.open h3 i { transform: rotate(45deg); color: var(--secondary); }
/* --- Responsive Interfaces --- */
@media (max-width: 1024px) {
.nav-container { display: none; } .hamburger { display: block; }
.grid-3 { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
.timeline { flex-wrap: wrap; gap: 20px; } .timeline::before { display: none; } .timeline .step { flex: none; width: 45%; }
#markets-table th:nth-child(5), #markets-table td:nth-child(5) { display:none; }
header { padding: 1rem; } main { padding: 32px 20px; }
.mobile-menu .dropdown-menu { position: static; display: block; background: rgba(0,0,0,0.2); box-shadow: none; border: none; border-radius: var(--radius-sm); margin-top: 8px; padding-left: 16px; opacity: 1; transform: none; }
.mobile-menu .dropdown-menu li a { color: rgba(255,255,255,0.9); padding: 8px 12px; }
}
@media (max-width: 768px) {
.grid-2, .grid-3, .scoring-grid, .simulator-results { grid-template-columns: 1fr; }
.timeline .step { width: 100%; } .visa-real { max-width: 100%; height: auto; min-height: 200px; }
.balance-amount { font-size: 2.2rem; } h1 { font-size: 2rem; } h2 { font-size: 1.5rem; }
.chart-header { flex-direction: column; align-items: flex-start; } .chart-container { height: 240px; }
#goals-container { grid-template-columns: 1fr !important; gap: 16px !important; }
.dca-plan, .account-card { flex-direction: column; align-items: flex-start; gap: 8px; }
.glass-widget { left: 10px; bottom: 90px; width: 180px; } #ws-status { width: 100% !important; margin-left: 0 !important; justify-content: center; margin-top: 8px; }
main { padding: 24px 16px; } .card { padding: 24px; } .header-left { gap: 10px; }
.auth-buttons button { padding: 8px 12px; font-size: 0.85rem; } .logo { font-size: 1.25rem; }
}
@media (max-width: 480px) {
.balance-amount { font-size: 1.8rem; } h1 { font-size: 1.75rem; } .card { padding: 16px; }
.btn { padding: 10px 16px; font-size: 0.9rem; } .phone-group { flex-direction: column; } .phone-group select, .phone-group input { width: 100%; }
.modal-content { padding: 20px; margin: 10px; width: calc(100% - 20px); } #crypto-float-widget { width: calc(100% - 40px); left: 20px; right: 20px; bottom: 20px; }
.stat-card-main, .balance-card { padding: 20px 16px; } .toast { width: 90%; right: 5%; }
}
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; } }
:focus-visible { outline: 2px solid var(--secondary); outline-offset: 2px; }
::-webkit-scrollbar { width: 8px; height: 8px; } ::-webkit-scrollbar-track { background: var(--bg-body); border-radius: var(--radius-full); }
::-webkit-scrollbar-thumb { background: var(--text-muted); border-radius: var(--radius-full); transition: var(--transition-fast); } ::-webkit-scrollbar-thumb:hover { background: var(--text-secondary); }
@keyframes circleSpin { 0% { transform: rotate(-90deg); } 100% { transform: rotate(270deg); } }
.circle-spin-anim { animation: circleSpin 1s linear infinite; }
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
</head>
<body>
<div id="loading-screen"><div class="loader"></div><div class="loader-text">Bit Wise</div></div>
<div class="toast-container" id="toast-container"></div>
<header id="main-header">
<div class="header-left">
<div class="logo" onclick="showPage('home')"><i class="fas fa-layer-group"></i> Bit<span>Wise</span></div>
<button class="hamburger" id="menu-toggle" aria-label="Menu"><i class="fas fa-bars"></i></button>
</div>
<div class="nav-container" id="public-nav">
<ul>
<li class="dropdown">
<a onclick="showPage('home')" class="active">Accueil <i class="fas fa-chevron-down" style="font-size:0.7em; margin-left:5px;"></i></a>
<ul class="dropdown-menu">
<li><a onclick="showPage('about')">À propos</a></li>
<li><a onclick="showPage('products')">Nos Offres</a></li>
<li><a onclick="showPage('faq')">FAQ</a></li>
</ul>
</li>
<li><a onclick="showPage('functioning')">Fonctionnement</a></li>
<li><a onclick="showPage('help')">Aide</a></li>
<li><a onclick="showPage('contact')">Contact</a></li>
</ul>
</div>
<div class="nav-container" id="client-nav" style="display:none;"><ul><li><a onclick="renderDashboard(); showPage('dashboard')">Tableau de bord</a></li><li><a onclick="renderProfile(); showPage('profile')">Paramètres</a></li><li><a onclick="logout()">Déconnexion</a></li></ul></div>
<div class="header-left">
<select id="lang-selector" aria-label="Langue">
<optgroup label="Europe"><option value="FR">🇫🇷 Français</option><option value="EN">🇬🇧 English</option><option value="DE">🇩🇪 Deutsch</option><option value="ES">🇪🇸 Español</option><option value="IT">🇮🇹 Italiano</option><option value="PT">🇵🇹 Português</option><option value="PT-BR">🇧🇷 Português (Brasil)</option><option value="NL">🇳🇱 Nederlands</option><option value="PL">🇵🇱 Polski</option><option value="SV">🇸🇪 Svenska</option><option value="NO">🇳🇴 Norsk</option><option value="DA">🇩🇰 Dansk</option><option value="FI">🇫🇮 Suomi</option><option value="IS">🇮🇸 Íslenska</option><option value="EL">🇬🇷 Ελληνικά</option><option value="CS">🇨🇿 Čeština</option><option value="SK">🇸🇰 Slovenčina</option><option value="HU">🇭🇺 Magyar</option><option value="RO">🇷🇴 Română</option><option value="BG">🇧🇬 Български</option><option value="HR">🇭🇷 Hrvatski</option><option value="SL">🇸🇮 Slovenščina</option><option value="SR">🇷🇸 Српски</option><option value="BS">🇧🇦 Bosanski</option><option value="MK">🇲🇰 Македонски</option><option value="SQ">🇦🇱 Shqip</option><option value="ET">🇪🇪 Eesti</option><option value="LV">🇱🇻 Latviešu</option><option value="LT">🇱🇹 Lietuvių</option><option value="UK">🇺🇦 Українська</option><option value="BE">🇧🇾 Беларуская</option><option value="MT">🇲🇹 Malti</option><option value="GA">🇮🇪 Gaeilge</option><option value="CY">🏴󠁧󠁢󠁷󠁬󠁳󠁿 Cymraeg</option><option value="GD">🏴󠁧󠁢󠁳󠁣󠁴󠁿 Gàidhlig</option><option value="LB">🇱🇺 Lëtzebuergesch</option><option value="CA">🇦🇩 Català</option><option value="EU">🏴 Euskara</option><option value="GL">🏴 Galego</option><option value="TR">🇹🇷 Türkçe</option><option value="RU">🇷🇺 Русский</option></optgroup>
<optgroup label="Asie"><option value="ZH">🇨🇳 中文 (简体)</option><option value="ZH-TW">🇹🇼 中文 (繁體)</option><option value="JA">🇯🇵 日本語</option><option value="KO">🇰🇷 한국어</option><option value="HI">🇮🇳 हिन्दी</option><option value="BN">🇧🇩 বাংলা</option><option value="UR">🇵🇰 اردو</option><option value="TA">🇮🇳 தமிழ்</option><option value="TE">🇮🇳 తెలుగు</option><option value="ML">🇮🇳 മലയാളം</option><option value="KN">🇮🇳 ಕನ್ನಡ</option><option value="GU">🇮🇳 ગુજરાતી</option><option value="PA">🇮🇳 ਪੰਜਾਬੀ</option><option value="MR">🇮🇳 मराठी</option><option value="NE">🇳🇵 नेपाली</option><option value="SI">🇱🇰 සිංහල</option><option value="MY">🇲🇲 မြန်မာ</option><option value="TH">🇹🇭 ไทย</option><option value="VI">🇻🇳 Tiếng Việt</option><option value="ID">🇮🇩 Bahasa Indonesia</option><option value="MS">🇲🇾 Bahasa Melayu</option><option value="TL">🇵🇭 Filipino</option><option value="JV">🇮🇩 Basa Jawa</option><option value="SU">🇮🇩 Basa Sunda</option><option value="KM">🇰🇭 ខ្មែរ</option><option value="LO">🇱🇦 ລາວ</option><option value="MN">🇲🇳 Монгол</option><option value="KK">🇰🇿 Қазақша</option><option value="UZ">🇺🇿 Oʻzbek</option><option value="KY">🇰🇬 Кыргызча</option><option value="TG">🇹🇯 Тоҷикӣ</option><option value="AZ">🇦🇿 Azərbaycan</option><option value="KA">🇬🇪 ქართული</option><option value="HY">🇦🇲 Հայերեն</option></optgroup>
<optgroup label="Moyen-Orient"><option value="AR">🇸🇦 العربية</option><option value="HE">🇮🇱 עברית</option><option value="FA">🇮🇷 فارسی</option><option value="PS">🇦🇫 پښتو</option></optgroup>
<optgroup label="Afrique"><option value="SW">🇰🇪 Kiswahili</option><option value="AM">🇪🇹 አማርኛ</option><option value="YO">🇳🇬 Yorùbá</option><option value="HA">🇳🇬 Hausa</option><option value="IG">🇳🇬 Igbo</option><option value="ZU">🇿🇦 isiZulu</option><option value="XH">🇿🇦 isiXhosa</option><option value="AF">🇿🇦 Afrikaans</option><option value="SO">🇸🇴 Soomaali</option><option value="RW">🇷🇼 Kinyarwanda</option><option value="SN">🇿🇼 chiShona</option><option value="NY">🇲🇼 Chichewa</option><option value="MG">🇲🇬 Malagasy</option></optgroup>
<optgroup label="Pacifique & Autres"><option value="HT">🇭🇹 Kreyòl Ayisyen</option><option value="HAW">🌺 ʻŌlelo Hawaiʻi</option><option value="MI">🇳🇿 Te Reo Māori</option><option value="SM">🇼🇸 Gagana Sāmoa</option><option value="CEB">🇵🇭 Cebuano</option><option value="ESP">🌐 Esperanto</option><option value="LA">📜 Latina</option></optgroup>
</select>
<button id="theme-toggle" class="btn-theme" aria-label="Toggle theme"><i class="fas fa-moon"></i></button>
<div class="auth-buttons" id="auth-btns"><button class="btn-login" onclick="showPage('login')">Connexion</button><button class="btn-register" onclick="showPage('register')">Inscription</button></div>
</div>
</header>
<div class="mobile-menu" id="mobile-menu">
<ul id="mobile-nav-list">
<li class="dropdown"><a>Accueil <i class="fas fa-chevron-down" style="font-size:0.8em; float:right; margin-top:5px;"></i></a>
<ul class="dropdown-menu">
<li><a onclick="showPage('home'); toggleMobileMenu()">Accueil</a></li>
<li><a onclick="showPage('about'); toggleMobileMenu()">À propos</a></li>
<li><a onclick="showPage('products'); toggleMobileMenu()">Nos Offres</a></li>
<li><a onclick="showPage('faq'); toggleMobileMenu()">FAQ</a></li>
</ul>
</li>
<li><a onclick="showPage('functioning'); toggleMobileMenu()">Fonctionnement</a></li>
<li><a onclick="showPage('help'); toggleMobileMenu()">Aide</a></li>
<li><a onclick="showPage('contact'); toggleMobileMenu()">Contact</a></li>
<li class="client-only" style="display:none;"><a onclick="renderDashboard(); showPage('dashboard'); toggleMobileMenu()">Tableau de bord</a></li>
<li class="client-only" style="display:none;"><a onclick="renderProfile(); showPage('profile'); toggleMobileMenu()">Paramètres</a></li>
<li class="client-only" style="display:none;"><a onclick="logout(); toggleMobileMenu()">Déconnexion</a></li>
</ul>
</div>
<main>
<section id="home" class="page-section active">
<div class="card scroll-animate" style="background: linear-gradient(135deg, var(--primary), #1e293b); color: white; text-align: center; padding: 60px 20px; border-radius: 15px;">
<i class="fas fa-university fa-3x" style="margin-bottom: 20px; color: var(--secondary);"></i>
<h1 style="color:white; font-size: 3rem;">Bit Wise : L'Excellence Bancaire</h1>
<p style="color: #cbd5e1; font-size: 1.2rem; max-width: 800px; margin: 0 auto;">Une institution financière moderne alliant sécurité, innovation et expertise humaine.</p>
</div>
<div class="grid-3 scroll-animate" style="margin-top: 40px;">
<div class="card">
<i class="fas fa-sitemap fa-2x" style="color:var(--secondary); margin-bottom:15px;"></i>
<h3>Organisation de l'espace</h3>
<p>Une interface intuitive conçue pour une navigation fluide entre vos comptes, épargne et investissements. Un tableau de bord centralisé pour une vision globale de votre patrimoine.</p>
</div>
<div class="card">
<i class="fas fa-file-contract fa-2x" style="color:var(--secondary); margin-bottom:15px;"></i>
<h3>Gestion administrative</h3>
<p>Simplifiez vos démarches : téléchargement de RIB, attestations de solde, certificats fiscaux et gestion des mandats SEPA directement depuis votre espace sécurisé.</p>
</div>
<div class="card">
<i class="fas fa-user-tie fa-2x" style="color:var(--secondary); margin-bottom:15px;"></i>
<h3>Compétences requises</h3>
<p>Notre équipe d'experts maîtrise les opérations de crédit, la gestion de patrimoine et les services d'investissement pour vous offrir un conseil personnalisé et pertinent.</p>
</div>
</div>
</section>
<section id="about" class="page-section">
<h1 class="scroll-animate">À Propos</h1>
<div class="card scroll-animate">
<p><strong>Bit Wise</strong> est bien plus qu'une simple application bancaire. Nous sommes une institution financière réglementée qui agit comme intermédiaire de confiance entre les épargnants et les emprunteurs.</p>
<p style="margin-top:16px;">Notre mission est de collecter les dépôts du public pour octroyer des crédits et fournir des services de paiement sécurisés, tout en accompagnant nos clients dans la réalisation de leurs projets de vie.</p>
</div>
<div class="card scroll-animate">
<h2><i class="fas fa-balance-scale" style="color:var(--secondary)"></i> Notre Philosophie</h2>
<p style="margin-top:12px;"><strong>Transparence, Sécurité et Innovation.</strong> Nous mettons la technologie au service de l'humain pour rendre la banque accessible, claire et efficace.</p>
</div>
</section>
<section id="products" class="page-section">
<h1 class="scroll-animate">Nos Offres et Services</h1>
<div class="card scroll-animate">
<h2><i class="fas fa-check-circle" style="color:var(--accent)"></i> Services de Base Inclus</h2>
<p style="margin:12px 0;">L'ouverture, la gestion et la clôture du compte sont simplifiées. Nos services essentiels comprennent :</p>
<ul style="padding-left:20px; line-height:1.9; color:var(--text-secondary);">
<li>La tenue du compte et l'envoi du relevé mensuel détaillé.</li>
<li>La fourniture immédiate d'un Relevé d'Identité Bancaire (RIB).</li>
<li>Les paiements par virement, prélèvement SEPA ou titre interbancaire.</li>
<li>Les dépôts et retraits d'espèces aux distributeurs partenaires.</li>
<li>La consultation à distance du solde 24h/24 et 7j/7.</li>
<li>Une carte bancaire à autorisation systématique pour maîtriser votre budget.</li>
<li>Deux chèques de banque par mois ou des moyens équivalents.</li>
</ul>
</div>
<div class="card scroll-animate">
<h2><i class="fas fa-credit-card" style="color:var(--secondary)"></i> Moyens de Paiement Premium</h2>
<p style="margin:12px 0;">Pour une liberté totale, accédez à nos services complets :</p>
<ul style="padding-left:20px; line-height:1.9; color:var(--text-secondary);">
<li>Chéquier personnalisé sur demande.</li>
<li>Cartes premium internationales (Visa Premier, MasterCard Gold).</li>
<li>Découvert autorisé (sous réserve d'acceptation).</li>
<li>Assistances voyage incluses.</li>
</ul>
</div>
<div class="card scroll-animate">
<h2><i class="fas fa-piggy-bank" style="color:var(--accent)"></i> Épargne et Placements</h2>
<p style="margin:12px 0;">Faites fructifier votre argent avec nos solutions adaptées :</p>
<ul style="padding-left:20px; line-height:1.9; color:var(--text-secondary);">
<li>Livrets réglementés (Livret A, LDDS, LEP).</li>
<li>Comptes à terme et Assurance-vie.</li>
<li>PEA (Plan d'Épargne en Actions) et Comptes-titres.</li>
</ul>
</div>
<div class="card scroll-animate">
<h2><i class="fas fa-hand-holding-usd" style="color:var(--secondary)"></i> Crédits</h2>
<p style="margin:12px 0;">Financez vos projets avec nos offres compétitives :</p>
<ul style="padding-left:20px; line-height:1.9; color:var(--text-secondary);">
<li>Prêts immobiliers taux fixe ou variable.</li>
<li>Crédits à la consommation personnels.</li>
<li>Crédits professionnels pour entreprises.</li>
</ul>
</div>
<div class="card scroll-animate">
<h2><i class="fas fa-briefcase" style="color:var(--accent)"></i> Services Annexes</h2>
<p style="margin:12px 0;">Un accompagnement global pour votre patrimoine :</p>
<ul style="padding-left:20px; line-height:1.9; color:var(--text-secondary);">
<li>Conseil en gestion de patrimoine dédié.</li>
<li>Services d'investissement boursier.</li>
<li>Assurances (habitation, vie, protection juridique).</li>
<li>Banque à distance via applications mobiles sécurisées.</li>
</ul>
</div>
</section>
<section id="faq" class="page-section">
<h1 class="scroll-animate" style="text-align:center; margin-bottom:30px;">Questions Fréquentes</h1>
<div class="card scroll-animate" style="max-width: 800px; margin: 0 auto;">
<div class="faq-item" onclick="this.classList.toggle('open')">
<h3>Comment ouvrir un compte chez Bit Wise ? <i class="fas fa-plus"></i></h3>
<p>Rendez-vous sur la page "Ouvrir un compte" via le menu, remplissez le formulaire d'inscription avec vos informations personnelles et joignez un justificatif d'identité valide. Votre compte est généralement activé sous 24h après vérification.</p>
</div>
<div class="faq-item" onclick="this.classList.toggle('open')">
<h3>Quels sont les frais de tenue de compte ? <i class="fas fa-plus"></i></h3>
<p>L'ouverture et la tenue de compte courant sont entièrement gratuites. Des frais peuvent s'appliquer uniquement sur les services optionnels (cartes premium, virements internationaux, assurances).</p>
</div>
<div class="faq-item" onclick="this.classList.toggle('open')">
<h3>Comment fonctionne la demande de crédit ? <i class="fas fa-plus"></i></h3>
<p>Utilisez notre simulateur intégré dans l'espace client pour estimer vos mensualités. Une fois votre dossier soumis avec les justificatifs requis, notre équipe l'analyse sous 24 à 48h. Vous suivez l'avancement en temps réel depuis votre tableau de bord.</p>
</div>
<div class="faq-item" onclick="this.classList.toggle('open')">
<h3>Mes données et transactions sont-elles sécurisées ? <i class="fas fa-plus"></i></h3>
<p>Absolument. Bit Wise utilise un chiffrement bancaire AES-256, une authentification à deux facteurs (2FA) et une surveillance continue des transactions. Vos données sont hébergées sur des serveurs conformes aux normes européennes (RGPD).</p>
</div>
<div class="faq-item" onclick="this.classList.toggle('open')">
<h3>Comment contacter le support client ? <i class="fas fa-plus"></i></h3>
<p>Notre équipe est disponible 24/7 via WhatsApp, Email, ou directement via le chat IA intégré. Vous trouverez tous les liens de contact dans le pied de page et dans le menu "Aide / Contact".</p>
</div>
</div>
</section>
<section id="functioning" class="page-section">
<h1 class="scroll-animate">Fonctionnement de Bit Wise</h1>
<div class="card scroll-animate">
<p>Bit Wise est une institution financière qui agit comme intermédiaire entre les épargnants et les emprunteurs, en collectant les dépôts du public pour octroyer des crédits et fournir des services de paiement.</p>
</div>
<div class="card scroll-animate">
<h2><i class="fas fa-cogs" style="color:var(--secondary)"></i> Nos Opérations Fondamentales</h2>
<p style="margin:12px 0;">Notre activité principale repose sur trois piliers définis par le code monétaire et financier :</p>
<ul style="padding-left:20px; line-height:1.9; color:var(--text-secondary);">
<li>La réception de fonds auprès du public (dépôts).</li>
<li>Les opérations de crédit (prêts).</li>
<li>Les services bancaires de paiement (virements, cartes).</li>
</ul>
<blockquote style="margin-top:20px; padding:16px 20px; border-left:4px solid var(--secondary); background:var(--bg-body); border-radius:var(--radius-md); font-style:italic; color:var(--text-primary);">
"La confiance est la monnaie la plus précieuse."
</blockquote>
</div>
</section>
<section id="help" class="page-section">
<h1 class="scroll-animate">Centre d'Aide</h1>
<div class="grid-3 scroll-animate">
<div class="card" style="cursor: pointer;" onclick="openSupportModal()">
<i class="fas fa-headset fa-2x" style="color:var(--secondary); margin-bottom:15px;"></i>
<h3>Support 24/7</h3>
<p>Une équipe dédiée disponible jour et nuit.</p>
<p style="margin-top:10px;"><strong>Canaux :</strong> Chat en direct, Email, WhatsApp</p>
<button class="btn btn-primary" style="margin-top:15px;">Cliquer pour contacter</button>
</div>
<div class="card">
<i class="fas fa-book fa-2x" style="color:var(--secondary); margin-bottom:15px;"></i>
<h3>Centre d'aide</h3>
<p>Retrouvez nos guides utilisateurs et notre FAQ détaillée pour répondre à toutes vos questions techniques et administratives.</p>
</div>
<div class="card">
<i class="fas fa-shield-alt fa-2x" style="color:var(--secondary); margin-bottom:15px;"></i>
<h3>Sécurité</h3>
<p>Vos données sont protégées par un chiffrement bancaire avancé (AES-256). Authentification forte et surveillance des transactions en temps réel.</p>
</div>
</div>
</section>
<section id="contact" class="page-section">
<h1 class="scroll-animate">Contactez-nous</h1>
<div class="grid-2 scroll-animate">
<div class="card">
<h3>Envoyez-nous un message</h3>
<form onsubmit="event.preventDefault(); showNotification('Message envoyé !', 'Nous vous répondrons sous 24h.', 'success'); this.reset();">
<label>Nom complet</label>
<input type="text" required placeholder="Votre nom">
<label>Email</label>
<input type="email" required placeholder="votre@email.com">
<label>Sujet</label>
<input type="text" required placeholder="Demande d'information">
<label>Message</label>
<textarea rows="5" required placeholder="Comment pouvons-nous vous aider ?"></textarea>
<button type="submit" class="btn btn-primary" style="width:100%; margin-top:12px;">Envoyer le message</button>
</form>
</div>
<div class="card">
<h3>Nos Coordonnées</h3>
<div class="info-row" style="margin-top:16px;"><i class="fas fa-map-marker-alt"></i><div>24 Avenue de l'Opéra, 75001 Paris</div></div>
<div class="info-row"><i class="fas fa-phone"></i><div><a href="https://wa.me/33753859610" target="_blank" rel="noopener" style="color:inherit; text-decoration:none;">+33 7 53 85 96 10</a></div></div>
<div class="info-row"><i class="fas fa-envelope"></i><div>contact@bitwise-bank.com</div></div>
<h3 style="margin-top:24px;">Horaires d'ouverture</h3>
<p style="margin-top:8px;">Lundi - Vendredi : 8h00 - 20h00<br>Samedi : 9h00 - 17h00</p>
</div>
</div>
</section>
<section id="legal-mentions" class="page-section"><div class="card legal-text-content scroll-animate"><h1>Mentions Légales</h1><p>Bit Wise SA - RCS Paris</p></div></section>
<section id="legal-privacy" class="page-section"><div class="card legal-text-content scroll-animate"><h1>Politique de confidentialité</h1><p>Vos données personnelles sont traitées conformément au RGPD.</p></div></section>
<section id="legal-cookies" class="page-section"><div class="card legal-text-content scroll-animate"><h1>Gestion des Cookies</h1><p>Bit Wise utilise des cookies pour améliorer votre expérience.</p></div></section>
<section id="legal-accessibility" class="page-section"><div class="card legal-text-content scroll-animate"><h1>Accessibilité</h1><p>Bit Wise s'engage à rendre son site accessible à toutes et tous.</p></div></section>
<section id="register" class="page-section"><div class="card scroll-animate" style="max-width: 640px; margin: auto;"><h2 style="text-align:center; margin-bottom: 20px;">Ouvrir un compte</h2><form id="regForm" onsubmit="handleRegister(event)" autocomplete="on">
<div class="grid-2"><input type="text" id="reg-nom" placeholder="Nom" autocomplete="family-name" required><input type="text" id="reg-prenom" placeholder="Prénom" autocomplete="given-name" required></div>
<input type="email" id="reg-email" placeholder="Email" autocomplete="email" required>
<div class="grid-2"><input type="password" id="reg-pass" placeholder="Mot de passe (8+ caractères)" autocomplete="new-password" minlength="8" required><input type="password" id="reg-pass2" placeholder="Confirmer le mot de passe" autocomplete="new-password" minlength="8" required></div>
<select id="reg-pays" required onchange="updatePhonePrefix()"><option value="" disabled selected>Pays de résidence</option></select>
<div class="phone-group" style="display:flex; gap:8px;"><select id="reg-phone-prefix" style="flex:0 0 130px;"></select><input type="tel" id="reg-tel" placeholder="Numéro de téléphone" autocomplete="tel-national" required style="flex:1;"></div>
<h4 style="margin:14px 0 6px;">Adresse de résidence</h4>
<div style="display:flex; gap:8px; align-items:center; margin-bottom:8px;"><input type="text" id="reg-address-search" placeholder="Rechercher mon adresse..." autocomplete="street-address" oninput="simulateAddressAutoComplete()" style="flex:1;"><button type="button" class="btn btn-secondary" onclick="toggleManualAddress()" id="manual-addr-btn" style="white-space:nowrap;">Saisie manuelle</button></div>
<div id="address-suggestions" style="display:none; border:1px solid var(--border); border-radius:8px; margin-bottom:8px; max-height:160px; overflow:auto;"></div>
<div id="address-details">
<div class="grid-2"><input type="text" id="reg-street-num" placeholder="Numéro de rue" autocomplete="address-line1"><input type="text" id="reg-street" placeholder="Nom de la rue" autocomplete="address-line2" required></div>
<div class="grid-2"><input type="text" id="reg-apt" placeholder="Appartement / étage (facultatif)" autocomplete="address-line3"><input type="text" id="reg-zip" placeholder="Code postal" autocomplete="postal-code" required></div>
<input type="text" id="reg-city" placeholder="Ville" autocomplete="address-level2" required>
</div>
<select id="reg-id-type" required><option value="" disabled selected>Document d'identité</option><option>CNI</option><option>Passeport</option><option>Permis de conduire</option></select>
<input type="file" id="reg-id" required>
<label style="display:flex; gap:8px; align-items:flex-start; margin-top:12px; font-size:0.9rem;"><input type="checkbox" id="reg-cgu" required style="margin-top:4px;"><span>J'accepte les conditions générales et la politique de confidentialité.</span></label>
<button type="submit" class="btn btn-primary" style="width:100%; margin-top:20px; padding:15px;">Valider</button>
</form></div></section>
<section id="login" class="page-section"><div class="card scroll-animate" style="max-width: 400px; margin: auto;"><h2 style="text-align:center">Espace Client</h2><form onsubmit="handleLogin(event)"><input type="email" id="login-email" placeholder="Email" required><input type="password" id="login-pass" placeholder="Mot de passe" required><button type="submit" class="btn btn-success" style="width:100%">Se connecter</button></form></div></section>
<section id="profile" class="page-section"><div class="card scroll-animate" style="max-width:720px; margin:auto;"><button type="button" class="btn btn-danger" style="margin-bottom:16px;" onclick="renderDashboard(); showPage('dashboard')">← Retour</button><div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;"><h2 style="margin:0;">Mes informations</h2><div style="display:flex; gap:6px;"><button type="button" class="btn btn-secondary" style="padding:6px 12px; font-size:0.85rem;" onclick="exportDocument('rib', 'pdf')"><i class="fas fa-file-pdf"></i> RIB PDF</button><button type="button" class="btn btn-secondary" style="padding:6px 12px; font-size:0.85rem;" onclick="exportDocument('rib', 'jpg')"><i class="fas fa-file-image"></i> RIB JPG</button></div></div><form id="profileForm" onsubmit="handleProfileSave(event)">
<div class="grid-2"><label>Nom<input type="text" id="prof-nom" required></label><label>Prénom<input type="text" id="prof-prenom" required></label></div>
<label>Email<input type="email" id="prof-email" required></label>
<div class="grid-2"><label>Pays<select id="prof-pays" onchange="updateProfilePhonePrefix()" required></select></label><label>Téléphone<div style="display:flex; gap:6px;"><select id="prof-phone-prefix" style="flex:0 0 110px;"></select><input type="tel" id="prof-tel" required style="flex:1;"></div></label></div>
<h4 style="margin:14px 0 6px;">Adresse</h4>
<div class="grid-2"><label>N° rue<input type="text" id="prof-street-num"></label><label>Rue<input type="text" id="prof-street" required></label></div>
<div class="grid-2"><label>Appartement<input type="text" id="prof-apt"></label><label>Code postal<input type="text" id="prof-zip" required></label></div>
<label>Ville<input type="text" id="prof-city" required></label>
<button type="submit" class="btn btn-primary" style="width:100%; margin-top:18px;">Enregistrer mes informations</button>
</form></div></section>
<section id="dashboard" class="page-section">
<div class="dashboard-clock-container scroll-animate"><i class="far fa-clock" style="font-size:1.5em; color:var(--secondary);"></i><div><div id="dash-clock-time" class="clock-time">--:--:--</div><div id="dash-clock-date" class="clock-date">Chargement...</div></div></div>
<div id="dash-home">
<div class="grid-3 scroll-animate">
<div class="card balance-card"><div id="dash-user-name" style="font-size: 1.15rem; font-weight: 600; margin-bottom: 8px; opacity: 0.95; letter-spacing: 0.5px;"></div><h3>Solde Disponible</h3><div class="balance-amount" id="dash-solde">0.00 €</div><div class="iban-display" id="dash-iban">FR76....</div><div class="iban-display" id="dash-bic" style="margin-top:6px; font-size:0.85rem;">BIC: ----</div></div>
<div class="card"><h3>Opérations</h3><button class="btn btn-dark" style="width:100%; margin-bottom:10px;" onclick="openAddBeneficiaryModal()"><i class="fas fa-user-plus"></i> Ajouter bénéficiaire</button><button class="btn btn-primary" style="width:100%; margin-bottom:10px;" onclick="openVirementModal('sepa')">💸 Virement SEPA</button><button class="btn btn-instant" style="width:100%; margin-bottom:10px;" onclick="openVirementModal('instant')"><i class="fas fa-bolt"></i> Instantané</button><button class="btn btn-secondary" style="width:100%; margin-bottom:10px;" onclick="toggleDashView('cards')">💳 Cartes</button><button class="btn btn-secondary" style="width:100%; margin-bottom:10px;" onclick="toggleDashView('credit')">🏦 Crédits</button><button class="btn btn-secondary" style="width:100%;" onclick="toggleDashView('savings')">🐷 Épargne & Objectifs</button></div>
<div class="card"><h3 style="display:flex; justify-content:space-between; align-items:center;">Derniers Mouvements <div style="display:flex; gap:6px;"><button class="btn-chart-export" title="Relevé PDF" onclick="exportDocument('releve', 'pdf')"><i class="fas fa-file-pdf"></i></button><button class="btn-chart-export" title="Relevé JPG" onclick="exportDocument('releve', 'jpg')"><i class="fas fa-file-image"></i></button></div></h3><div class="transaction-list" id="trans-history"></div></div>
</div>
<div class="grid-2" style="margin-top: 24px;">
<div class="card chart-card scroll-animate"><div class="chart-header"><div class="chart-title"><i class="fas fa-chart-line" style="color:var(--secondary);"></i> Évolution Solde</div><div class="chart-filters"><button class="chart-filter active" data-days="30">30j</button></div></div><div class="chart-container"><canvas id="balanceChart"></canvas></div></div>
<div class="card chart-card scroll-animate"><div class="chart-header"><div class="chart-title"><i class="fas fa-chart-pie" style="color:var(--accent);"></i> Dépenses</div></div><div class="chart-container"><canvas id="expenseChart"></canvas></div></div>
</div>
</div>
<div id="dash-cards" style="display:none;"><button class="btn btn-danger" onclick="toggleDashView('home')">← Retour</button><h2 style="margin-top: 20px;">Mes Cartes Bancaires</h2><div class="grid-2" id="cards-container"></div></div>
<div id="dash-credit" style="display:none;">
<button class="btn btn-danger" onclick="toggleDashView('home')">← Retour</button>
<div class="credit-header">
<h2><i class="fas fa-landmark"></i> Espace Crédit</h2>
<p style="color: var(--text-secondary); margin-top: 5px; margin-bottom: 20px;">Simulez, évaluez et gérez vos projets de financement en toute transparence.</p>
</div>
<div class="card credit-card scroll-animate" id="credit-scoring-section">
<div class="section-header"><h3>Évaluation & Éligibilité</h3><span class="badge warning" id="eligibility-badge" style="display:none;">Éligibilité conditionnelle</span></div>
<div class="scoring-grid" style="display: flex; flex-wrap: wrap; justify-content: space-around; align-items: center; gap: 20px;">
<div class="score-display" style="text-align: center;">
<div class="score-circle-wrapper" style="position: relative; width: 120px; height: 120px; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
<svg class="score-circle circle-spin-anim" id="score-circle-svg" width="120" height="120" viewBox="0 0 120 120" style="position: absolute; top: 0; left: 0; transform: rotate(-90deg);">
<circle cx="60" cy="60" r="54" fill="none" stroke="var(--bg-body)" stroke-width="8"></circle>
<circle id="score-circle-progress" cx="60" cy="60" r="54" fill="none" stroke="var(--text-muted)" stroke-width="8" stroke-dasharray="339.292" stroke-dashoffset="339.292" stroke-linecap="round" style="transition: stroke-dashoffset 1s ease-out, stroke 0.5s ease-in-out;"></circle>
</svg>
<div class="score-text" style="position: relative; z-index: 1;">
<span id="score-value" style="font-size: 24px; font-weight: bold; color: var(--text-primary);">0</span><br>
<span style="font-size: 14px; color: var(--text-secondary);">/ 850</span>
</div>
</div>
<div style="margin-top: 10px; font-weight: bold;">Score de Crédit</div>
</div>
<div style="flex: 1; min-width: 200px;">
<div class="info-row" style="margin-bottom: 20px;"><i class="fas fa-wallet"></i><div><strong>Plafond d'emprunt estimé</strong><br><span id="max-borrow-limit">Jusqu'à 30 000 €</span></div></div>
<div class="info-row"><i class="fas fa-chart-line"></i><div><strong>Taux d'endettement max</strong><br><span>33%</span></div></div>
</div>
</div>
</div>
<div class="card credit-card scroll-animate" id="credit-form-section">
<div class="section-header"><h3>Simulateur de Crédit <span style="color:var(--danger); font-size:0.85em; margin-left:8px;">* Champs obligatoires</span></h3></div>
<div class="grid-3">
<div>
<label>Montant (€) <span style="color:var(--danger);">*</span></label>
<input type="number" id="loan-amount" placeholder="15000" oninput="calcLoanRealTime()" required>
</div>
<div>
<label>Durée (mois) <span style="color:var(--danger);">*</span></label>
<select id="loan-duration" onchange="calcLoanRealTime()" required>
<option value="12">12 mois (1 an)</option><option value="24">24 mois (2 ans)</option><option value="36">36 mois (3 ans)</option>
<option value="48">48 mois (4 ans)</option><option value="60" selected>60 mois (5 ans)</option><option value="72">72 mois (6 ans)</option>
<option value="84">84 mois (7 ans)</option><option value="96">96 mois (8 ans)</option><option value="108">108 mois (9 ans)</option>
<option value="120">120 mois (10 ans)</option><option value="132">132 mois (11 ans)</option><option value="144">144 mois (12 ans)</option>
<option value="156">156 mois (13 ans)</option><option value="168">168 mois (14 ans)</option><option value="180">180 mois (15 ans)</option>
<option value="192">192 mois (16 ans)</option><option value="204">204 mois (17 ans)</option><option value="216">216 mois (18 ans)</option>
<option value="228">228 mois (19 ans)</option><option value="240">240 mois (20 ans)</option>
</select>
</div>
<div>
<label>Taux d'intérêt (%)</label>
<input type="number" id="loan-rate" value="3.0" min="2.0" max="5.0" step="0.1" oninput="calcLoanRealTime()">
</div>
</div>
<div class="grid-2" style="margin-top: 16px;">
<div>
<label>Justificatif de revenu <span style="color:var(--danger);">*</span></label>
<select id="loan-income-proof" required>
<option value="" disabled selected>Choisir un justificatif...</option>
<option value="Fiche de pension">Une fiche de pension</option>
<option value="Relevé bancaire">Un Relevé bancaire</option>
<option value="RSA">Un RSA</option>
<option value="Autre">Autre</option>
</select>
</div>
<div>
<label>Option télécharger le document <span style="color:var(--danger);">*</span></label>
<input type="file" id="loan-document" accept=".pdf,.png,.jpg,.jpeg" required>
</div>
</div>
<div class="simulator-results" id="sim-results">
<div class="result-card"><small>Mensualité hors assurance</small><strong id="loan-monthly">0,00 €</strong></div>
<div class="result-card"><small>Assurance (0,36%/an)</small><strong id="loan-insurance">0,00 €</strong></div>
<div class="result-card highlight"><small>Coût total mensuel en temps réel</small><strong id="loan-total-monthly">0,00 €</strong></div>
</div>
<div class="debt-ratio-container">
<div class="ratio-header"><span>Taux d'endettement calculé</span><strong id="debt-ratio-value">0%</strong></div>
<div class="ratio-bar"><div class="ratio-fill" id="debt-ratio-fill"></div></div>
<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
<div class="ratio-status" id="debt-ratio-status">Éligibilité: En attente</div>
<button class="btn btn-primary" id="btn-apply-loan" onclick="applyLoan()" style="padding: 6px 12px; font-size: 0.85rem; background: #3b82f6; color: white; display: flex; align-items: center; gap: 6px;" disabled>
<i class="fab fa-telegram"></i> Demander ce crédit
</button>
</div>
</div>
<div style="background: var(--bg-body); padding: 16px; border-radius: var(--radius-md); margin-bottom: 24px; border: 1px solid var(--border);">
<h4><i class="far fa-calendar-alt" style="color:var(--secondary)"></i> Calendrier de Remboursement</h4>
<p style="margin: 8px 0 0; color: var(--text-muted); font-size: 0.9rem;">1ère échéance fixée au 1er du mois suivant la demande</p>
</div>
<div style="background: var(--bg-body); padding: 16px; border-radius: var(--radius-md); margin-bottom: 24px; border: 1px solid var(--border);" id="credit-history-section">
<div style="display:flex; justify-content:space-between; align-items:center;">
<h4 style="margin:0;"><i class="fas fa-history" style="color:var(--secondary)"></i> Historique des demandes de crédit</h4>
<div style="display:flex; gap:6px;">
<button class="btn-chart-export" title="Exporter PDF" onclick="exportDocument('historique_demandes', 'pdf')"><i class="fas fa-file-pdf"></i></button>
<button class="btn-chart-export" title="Exporter JPG" onclick="exportDocument('historique_demandes', 'jpg')"><i class="fas fa-file-image"></i></button>
</div>
</div>
<div id="credit-history-list" style="margin-top: 12px; font-size: 0.9rem;">
<p style="color: var(--text-muted); font-style: italic;">Aucune demande de crédit.</p>
</div>
</div>
<div style="background: var(--bg-body); padding: 16px; border-radius: var(--radius-md); margin-bottom: 24px; border: 1px solid var(--border);" id="credit-status-band">
<h4><i class="fas fa-info-circle" style="color:var(--secondary)"></i> État de la demande</h4>
<div id="credit-status-text" style="margin-top: 12px; font-size: 0.9rem;">
<p style="color: var(--text-muted); font-weight: 500;">Aucune demande en cours.</p>
</div>
</div>
</div>
<div class="card credit-card scroll-animate" id="credit-tracking-section" style="display:none;">
<div class="section-header"><h3>Suivi de votre demande de crédit <span onclick="devFastForward()" style="cursor:pointer; opacity:0.1; font-size:12px;" title="Avance rapide 1h">⏱️</span></h3></div>
<div id="credit-tracking-progress-container">
<p style="margin-bottom: 8px;">Progression de l'étude de votre dossier : <strong id="credit-tracking-pct">0%</strong></p>
<div class="progress-modern">
<div class="progress-track"><div class="progress-fill" id="credit-tracking-bar" style="width: 0%;"></div></div>
</div>
<p style="font-size:0.85rem; color:var(--text-muted); margin-top:8px;">Le traitement de votre demande peut prendre plusieurs heures.</p>
</div>
<div id="credit-validation-message" style="display:none; margin-top: 20px;">
<div class="info-banner" style="background:#dcfce7; border-color:#22c55e; color:#166534; margin-bottom: 16px;">
<i class="fas fa-check-circle" style="font-size:1.5rem; margin-right:10px;"></i>
<strong>Votre demande crédit est validée !</strong>
</div>
<p style="margin-bottom:12px;">Le montant de <strong><span id="credit-amount-display"></span> €</strong> a été crédité sur votre compte crédit N° <strong><span id="credit-account-number"></span></strong>.</p>
<p style="margin-bottom:20px;">Statut des fonds : <span class="badge rejected" style="font-size:0.9rem;">BLOQUÉ</span></p>
<div id="credit-contract-section" style="padding: 16px; border: 1px solid var(--border); border-radius: var(--radius-md); background: var(--bg-body);">
<h4 style="margin-bottom:8px;"><i class="fas fa-file-signature"></i> Signature du contrat de crédit</h4>
<p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom:12px;">Un code est requis pour signer le contrat et débloquer les fonds. Le code a été envoyé à l'administrateur. Le contrat a été envoyé par e-mail.</p>
<div style="display:flex; gap:10px;">
<input type="text" id="credit-contract-code" placeholder="Code de signature (ex: 123456)">
<button class="btn btn-success" style="white-space:nowrap;" onclick="signCreditContract()">Signer et Débloquer</button>
</div>
</div>
</div>
<div id="credit-unblocked-section" style="display:none; margin-top: 20px;">
<div class="info-banner" style="background:#eff6ff; border-color:#3b82f6; color:#1d4ed8; margin-bottom: 16px;">
<i class="fas fa-unlock-alt" style="font-size:1.2rem; margin-right:10px;"></i> Fonds débloqués sur le compte crédit.
</div>
<button class="btn btn-primary" style="width:100%; background: linear-gradient(135deg, #2563eb, #1d4ed8); color: white; padding: 14px; font-size: 1.05rem;" id="btn-transfer-main" onclick="startMainTransfer()">
<i class="fas fa-exchange-alt" style="margin-right:8px;"></i> Transféré vers le solde principale
</button>
</div>
<div id="credit-transfer-section" style="display:none; margin-top: 20px;">
<p style="margin-bottom: 8px;">Transfert vers le solde principal : <strong id="credit-transfer-pct">0%</strong></p>
<div class="progress-modern">
<div class="progress-track"><div class="progress-fill" id="credit-transfer-bar" style="width: 0%; background: linear-gradient(90deg, #3b82f6, #2563eb);"></div></div>
</div>
<div id="credit-insurance-section" style="display:none; margin-top: 20px; padding: 16px; border: 1px solid var(--warning); border-radius: var(--radius-md); background: #fffbeb;">
<h4 style="color: #92400e; margin-bottom:8px;"><i class="fas fa-shield-alt"></i> Signature de la Police d'assurance crédit</h4>
<p style="font-size: 0.9rem; color: #92400e; margin-bottom:12px;">Une validation supplémentaire est requise. Un code de signature a été envoyé à l'administrateur.</p>
<div style="display:flex; gap:10px;">
<input type="text" id="credit-insurance-code" placeholder="Code assurance (ex: 654321)">
<button class="btn" style="background:var(--warning); color:white; white-space:nowrap;" onclick="signInsuranceContract()">Signer la police d'assurance</button>
</div>
</div>
</div>
<div id="credit-final-success" style="display:none; margin-top: 20px; text-align:center;">
<i class="fas fa-check-circle" style="font-size: 4rem; color: var(--accent); margin-bottom: 16px;"></i>
<h3>Transfert terminé avec succès</h3>
<p style="color: var(--text-muted); margin-top: 8px;">Les fonds ont été ajoutés à votre solde principal.</p>
<button class="btn btn-dark" style="margin-top: 16px;" onclick="toggleDashView('home')">Retour au tableau de bord</button>
</div>
</div>
</div>
<div id="dash-savings" style="display:none;">
<button class="btn btn-danger" onclick="toggleDashView('home')">← Retour</button>
<h2 style="margin-top:20px;">Épargne & Objectifs</h2>
<div class="card" style="background: linear-gradient(to right, #10b981, #059669); color: white;"><h3>Solde Total Épargne</h3><div style="font-size: 2.5rem; font-weight: bold;" id="total-savings-display">0.00 €</div></div>
<h3 style="margin-top:20px;">Mes Objectifs</h3>
<div class="grid-3 scroll-animate" id="goals-container"></div>
<div style="margin-top: 32px; text-align: center;"><button class="btn btn-crypto" onclick="toggleDashView('crypto'); initCryptoModule();" style="width: 100%; max-width: 400px; padding: 16px; font-size: 1.05rem;"><i class="fab fa-bitcoin"></i> Accéder au module Crypto & Investissement</button></div>
</div>
<div id="dash-crypto" style="display:none;">
<button class="btn btn-danger" onclick="toggleDashView('home')">← Retour</button>
<div class="grid-2" style="margin-top:20px;">
<div class="card scroll-animate"><div class="chart-header"><div class="chart-title"><i class="fas fa-wallet" style="color:var(--accent)"></i> Portfolio</div></div><div style="text-align:center;font-size:2rem;font-weight:700;" id="crypto-total-value">0.00 $</div><div class="chart-container"><canvas id="portfolioChart"></canvas></div></div>
<div class="card scroll-animate"><h3>Actions Rapides</h3><div class="grid-2" style="gap:10px;"><button class="btn btn-success" onclick="openCryptoAction('buy')">Acheter</button><button class="btn btn-danger" onclick="openCryptoAction('sell')">Vendre</button><button class="btn btn-instant" onclick="openCryptoAction('stake')">Staker</button><button class="btn btn-primary" onclick="openCryptoAction('convert')">Convertir</button></div></div>
</div>
<div class="card scroll-animate" style="margin-top:20px;"><div class="chart-header"><div class="chart-title"><i class="fas fa-chart-line" style="color:var(--secondary)"></i> Marchés</div><div class="chart-filters"><button class="chart-filter active" onclick="filterMarkets('all')">Tous</button><button class="chart-filter" onclick="filterMarkets('gainers')">Gainers</button><button class="chart-filter" onclick="filterMarkets('losers')">Losers</button></div></div><div class="table-wrapper" style="max-height:300px;"><table class="credit-table"><thead><tr><th>#</th><th>Actif</th><th>Prix</th><th>24h</th><th>Action</th></tr></thead><tbody id="markets-body"></tbody></table></div></div>
<div class="card scroll-animate" style="margin-top:20px;"><div class="chart-header"><div class="chart-title"><i class="fas fa-star" style="color:var(--warning)"></i> Watchlist</div><button class="btn-chart-export" onclick="openWatchlistManager()"><i class="fas fa-cog"></i> Gérer</button></div><div id="watchlist-container" style="margin-top:12px;"></div></div>
<div class="card scroll-animate" style="margin-top:20px;"><h3>Terminal Trading</h3><div class="grid-2"><div class="card" style="background:var(--bg-body);padding:10px;height:200px;overflow:auto;font-family:monospace;" id="order-book"></div><div><label>Prix <input type="number" id="order-price" placeholder="64200"></label><label>Qté <input type="number" id="order-qty" placeholder="0.01"></label><div style="display:flex;gap:8px;margin-top:8px;"><button class="btn btn-success" onclick="placeAdvancedOrder('buy')" style="flex:1;">Buy</button><button class="btn btn-danger" onclick="placeAdvancedOrder('sell')" style="flex:1;">Sell</button></div></div></div></div>
<div class="card scroll-animate" style="margin-top:20px;"><h3>PnL Temps Réel</h3><div class="grid-2"><div id="pnl-stats" style="background:var(--bg-body);padding:12px;border-radius:var(--radius-md);"><small>Investi</small><div id="pnl-invested" style="font-size:1.3rem;font-weight:700;">0 $</div><small>Profit</small><div id="pnl-diff" style="font-size:1.8rem;font-weight:800;">+0%</div></div><div class="chart-container"><canvas id="pnlChart"></canvas></div></div></div>
<div class="card scroll-animate" style="margin-top:20px;"><div class="chart-header"><div class="chart-title"><i class="fas fa-tools" style="color:var(--secondary)"></i> Outils</div></div><div style="display:flex;flex-wrap:wrap;gap:10px;"><button class="btn btn-dark" onclick="exportCryptoHistoryToCSV()"><i class="fas fa-file-csv"></i> Export CSV</button><button class="btn btn-chart-export" onclick="openFeeCalculator()"><i class="fas fa-calculator"></i> Frais</button><button class="btn btn-chart-export" onclick="openDCAModal()"><i class="fas fa-sync-alt"></i> DCA</button><div id="ws-status" style="margin-left:auto;display:flex;align-items:center;gap:8px;font-size:0.8rem;padding:6px 10px;background:var(--bg-body);border-radius:var(--radius-md);"><span class="ws-dot"></span><span>Connexion</span></div></div></div>
<div class="glass-widget" id="crypto-float-widget"><div class="widget-header" onclick="toggleWidgetExpand()"><i class="fab fa-bitcoin" style="color:#f7931a;"></i> <span id="float-btc-price">$--</span> <span id="float-btc-change">--%</span><i class="fas fa-chevron-up" style="margin-left:auto;transition:0.3s;" id="float-arrow"></i></div><div class="widget-body" id="float-widget-body"><div class="float-item"><span>ETH</span><span id="float-eth-price">$--</span></div><div class="float-item"><span>SOL</span><span id="float-sol-price">$--</span></div></div></div>
</div>
</section>
</main>
<footer><div class="footer-grid scroll-animate"><div class="footer-col"><h4>Navigation</h4><ul><li onclick="showPage('home')">Accueil</li><li onclick="showPage('products')">Nos Offres</li><li onclick="showPage('functioning')">Fonctionnement</li></ul></div><div class="footer-col"><h4>Support</h4><ul><li onclick="showPage('help')">Centre d'aide</li><li onclick="showPage('contact')">Nous contacter</li><li onclick="openSupportModal()">Chat en direct</li></ul></div><div class="footer-col"><h4>Légal</h4><ul><li onclick="showPage('legal-mentions')">Mentions légales</li><li onclick="showPage('legal-privacy')">Politique de confidentialité</li><li onclick="showPage('legal-cookies')">Gestion des Cookies</li><li onclick="showPage('legal-accessibility')">Accessibilité</li></ul></div></div><div class="legal-bar scroll-animate"><p>2026 Bit Wise – Société Anonyme au capital de 18 000 000 € • RCS Paris 803 542 709 • Siège : 24 Avenue de l'Opéra, 75001 Paris</p><p>Établissement de crédit agréé par l'ACPR – N° 49375 • Adhérent au FGDR jusqu'à 200 000 € par déposant.</p><p class="legal-links"><a onclick="showPage('legal-mentions')">Mentions légales</a> | <a onclick="showPage('legal-privacy')">Confidentialité</a> | <a onclick="showPage('legal-cookies')">Cookies</a> | <a onclick="showPage('legal-accessibility')">Accessibilité</a></p></div></footer>
<div class="floating-icons"><div class="mail-icon" onclick="showPage('contact')"><i class="fas fa-envelope"></i></div><a href="https://wa.me/33753859610" target="_blank" rel="noopener" class="wa-icon" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a></div>
<div id="back-to-top"><i class="fas fa-arrow-up"></i></div>
<!-- MODALS -->
<div id="card-pin-modal" class="modal"><div class="modal-content" style="max-width:400px;"><h3 id="card-pin-title" style="margin-bottom:12px;">Code PIN de la carte</h3><input type="password" id="card-pin-input" maxlength="4" placeholder="****" style="text-align:center;letter-spacing:4px;font-size:1.5rem;margin-bottom:12px;" inputmode="numeric"><button class="btn btn-success" style="width:100%;" onclick="confirmCardPin()">Valider</button><button class="btn btn-danger" style="width:100%;margin-top:10px;" onclick="closeModal('card-pin-modal')">Annuler</button></div></div>
<div id="card-view-modal" class="modal"><div class="modal-content" style="max-width:400px; text-align:center;"><h3 style="margin-bottom:16px;">Informations de la carte</h3><div style="background:var(--bg-body);padding:20px;border-radius:12px;border:1px solid var(--border);margin-bottom:16px;"><div style="font-family:monospace;font-size:1.4rem;letter-spacing:2px;margin-bottom:12px;" id="card-view-pan">---- ---- ---- ----</div><div style="display:flex;justify-content:space-between;font-family:monospace;font-size:1rem;"><div style="text-align:left;"><small style="display:block;color:var(--text-muted);font-family:sans-serif;">EXP</small><span id="card-view-exp">--/--</span></div><div style="text-align:right;"><small style="display:block;color:var(--text-muted);font-family:sans-serif;">CVV</small><span id="card-view-cvv">---</span></div></div></div><button class="btn btn-dark" style="width:100%;" onclick="closeModal('card-view-modal')">Fermer</button></div></div>
<div id="card-limit-modal" class="modal"><div class="modal-content" style="max-width:400px;"><h3 style="margin-bottom:12px;">Gérer le plafond</h3><p style="text-align:center; font-size:1.5rem; font-weight:700; margin-bottom:12px;" id="card-limit-display">1000 €</p><input type="range" id="card-limit-input" min="100" max="5000" step="100" style="width:100%;margin-bottom:16px;" oninput="updateLimitDisplay()"><button class="btn btn-success" style="width:100%;" onclick="confirmCardLimit()">Valider</button><button class="btn btn-danger" style="width:100%;margin-top:10px;" onclick="closeModal('card-limit-modal')">Annuler</button></div></div>
<div id="otp-modal" class="modal"><div class="modal-content"><h3>Validation de l'inscription</h3><p style="color:var(--text-muted);font-size:0.9rem;margin-bottom:12px;">Voici votre code de validation. Saisissez-le ci-dessous pour finaliser l'ouverture de votre compte.</p><div id="otp-display" style="margin:0 0 16px;padding:18px;background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;text-align:center;font-size:2rem;letter-spacing:8px;font-weight:700;color:#1d4ed8;font-family:monospace;">------</div><input type="text" id="otp-input" placeholder="Code" inputmode="numeric" maxlength="6"><button class="btn btn-success" onclick="verifyOTP()">Valider</button></div></div>
<div id="add-beneficiary-modal" class="modal"><div class="modal-content"><h3>Ajouter un bénéficiaire</h3><input type="text" id="new-ben-name-dash" placeholder="Nom"><input type="text" id="new-ben-firstname-dash" placeholder="Prénom"><input type="text" id="new-ben-iban-dash" placeholder="IBAN"><input type="text" id="new-ben-bic-dash" placeholder="BIC / Swift"><button class="btn btn-success" style="width:100%" onclick="saveNewBeneficiary()">Enregistrer</button><button class="btn btn-danger" style="width:100%; margin-top:10px;" onclick="closeModal('add-beneficiary-modal')">Annuler</button></div></div>
<div id="virement-modal" class="modal"><div class="modal-content"><h3 id="virement-title">Virement</h3><select id="virement-beneficiary" onchange="applyBeneficiarySelection()"><option value="">Choisir un bénéficiaire...</option></select><input type="text" id="virement-name-manual" placeholder="Nom"><input type="text" id="virement-firstname-manual" placeholder="Prénom"><input type="text" id="virement-iban-manual" placeholder="IBAN"><input type="text" id="virement-bic-manual" placeholder="BIC / Swift"><input type="number" id="virement-amount" placeholder="Montant"><button class="btn btn-primary" style="width:100%" onclick="startSecureTransfer()">Valider</button><button class="btn btn-danger" style="width:100%; margin-top:10px;" onclick="closeModal('virement-modal')">Annuler</button></div></div>
<div id="support-modal" class="modal"><div class="modal-content"><h3>Support 24/7</h3><p style="color:var(--text-muted);font-size:0.9rem;margin-bottom:16px;">Choisissez votre canal de communication préféré.</p><a href="https://wa.me/33753859610" target="_blank" rel="noopener" class="support-option" onclick="closeModal('support-modal')"><i class="fab fa-whatsapp support-icon" style="color:#25D366;"></i><div><strong>WhatsApp</strong><div style="font-size:0.85rem;color:var(--text-muted);">Discuter avec un conseiller</div></div></a><a href="mailto:contact@bitwise-bank.com" class="support-option" onclick="closeModal('support-modal')"><i class="fas fa-envelope support-icon" style="color:#EA4335;"></i><div><strong>E-mail</strong><div style="font-size:0.85rem;color:var(--text-muted);">contact@bitwise-bank.com</div></div></a><a href="javascript:void(0)" class="support-option" onclick="openAIChat()"><i class="fas fa-comments support-icon" style="color:var(--secondary);"></i><div><strong>Message</strong><div style="font-size:0.85rem;color:var(--text-muted);">Chat avec l'assistant IA</div></div></a><button class="btn btn-dark" style="width:100%; margin-top:15px;" onclick="closeModal('support-modal')">Fermer</button></div></div>
<div id="ai-chat-modal" class="modal"><div class="modal-content" style="max-width:480px;padding:0;display:flex;flex-direction:column;height:600px;max-height:90vh;"><div class="ai-chat-header"><div class="ai-chat-title"><div class="ai-chat-avatar"><i class="fas fa-robot"></i></div><div><strong>Assistant Bit Wise</strong><div style="font-size:0.8rem;color:var(--text-muted);display:flex;align-items:center;gap:6px;"><span class="ai-status-dot"></span>En ligne</div></div></div><button class="ai-chat-close" onclick="closeModal('ai-chat-modal')" aria-label="Fermer"><i class="fas fa-times"></i></button></div><div class="ai-chat-body" id="ai-chat-messages"></div><div class="ai-chat-input-bar"><input type="text" id="ai-chat-input" placeholder="Écrivez votre message..." autocomplete="off" onkeydown="if(event.key==='Enter')sendAIChatMessage()"><button class="ai-chat-send" onclick="sendAIChatMessage()" aria-label="Envoyer"><i class="fas fa-paper-plane"></i></button></div></div></div>
<div id="goal-action-modal" class="modal"><div class="modal-content" style="max-width:400px;"><h3 id="goal-action-title" style="text-align:center;margin-bottom:16px;">Action</h3><div id="goal-action-balance-info" style="background:var(--bg-body);padding:10px;border-radius:8px;text-align:center;margin-bottom:16px;font-size:0.9rem;"></div><input type="number" id="goal-action-amount" placeholder="0.00" min="0.01" step="0.01"><button id="goal-action-confirm" class="btn btn-success" style="width:100%;margin-top:10px;">Confirmer</button><button class="btn btn-danger" style="width:100%;margin-top:10px;" onclick="closeModal('goal-action-modal')">Annuler</button></div></div>
<div id="crypto-action-modal" class="modal"><div class="modal-content" style="max-width:400px;"><h3 id="crypto-action-title" style="text-align:center;margin-bottom:16px;">Action</h3><select id="crypto-asset-select" style="margin-bottom:12px;"></select><input type="number" id="crypto-action-amount" placeholder="Montant / Quantité" step="0.0001" min="0"><div id="crypto-action-preview" style="background:var(--bg-body);padding:10px;border-radius:8px;margin:10px 0;font-size:0.9rem;text-align:center;">Estimation: <strong>0.00 $</strong></div><button id="crypto-action-confirm" class="btn btn-success" style="width:100%;">Confirmer</button><button class="btn btn-danger" style="width:100%;margin-top:10px;" onclick="closeModal('crypto-action-modal')">Annuler</button></div></div>
<div id="price-alert-modal" class="modal"><div class="modal-content" style="max-width:400px;"><h3 style="margin-bottom:12px;">🔔 Alerte Prix</h3><select id="alert-asset" style="margin-bottom:10px;"></select><div style="display:flex;gap:8px;margin-bottom:12px;"><select id="alert-type" style="width:40%;"><option value="above">📈 Au-dessus</option><option value="below">📉 En dessous</option></select><input type="number" id="alert-target" placeholder="Prix" step="0.01" style="width:60%;"></div><button class="btn btn-primary" style="width:100%;" onclick="savePriceAlert()">Activer</button><div id="active-alerts-list" style="margin-top:12px;max-height:100px;overflow-y:auto;"></div><button class="btn btn-danger" style="width:100%;margin-top:10px;" onclick="closeModal('price-alert-modal')">Fermer</button></div></div>
<div id="dca-modal" class="modal"><div class="modal-content" style="max-width:400px;"><h3 style="margin-bottom:12px;">🔄 DCA</h3><select id="dca-asset" style="margin-bottom:10px;"></select><div style="display:flex;gap:8px;margin-bottom:12px;"><input type="number" id="dca-amount" placeholder="Montant ($)" step="10" min="10" style="width:60%;"><select id="dca-frequency" style="width:40%;"><option value="daily">Quotidien</option><option value="weekly">Hebdo</option><option value="monthly" selected>Mensuel</option></select></div><button class="btn btn-success" style="width:100%;" onclick="saveDCA()">Activer</button><button class="btn btn-danger" style="width:100%;margin-top:10px;" onclick="closeModal('dca-modal')">Annuler</button></div></div>
<div id="fee-calc-modal" class="modal"><div class="modal-content" style="max-width:400px;"><h3 style="margin-bottom:12px;">🧮 Frais</h3><select id="fee-network" style="margin-bottom:10px;"><option value="bitcoin">Bitcoin</option><option value="ethereum">Ethereum</option><option value="solana">Solana</option></select><div style="display:flex;gap:8px;margin-bottom:12px;"><select id="fee-speed" style="width:40%;"><option value="medium" selected>Moyen</option><option value="high">Rapide</option></select><input type="number" id="fee-amount" placeholder="Montant ($)" style="width:60%;"></div><div id="fee-results" style="background:var(--bg-body);padding:10px;border-radius:8px;margin-bottom:12px;display:none;"></div><button class="btn btn-success" style="width:100%;" onclick="calculateNetworkFee()">Calculer</button><button class="btn btn-danger" style="width:100%;margin-top:10px;" onclick="closeModal('fee-calc-modal')">Fermer</button></div></div>
<div id="twofa-setup-modal" class="modal"><div class="modal-content" style="max-width:400px;"><h3 style="margin-bottom:12px;">🔐 2FA</h3><div style="background:var(--bg-body);padding:12px;border-radius:8px;margin-bottom:12px;text-align:center;font-family:monospace;font-size:1.3rem;letter-spacing:3px;" id="twofa-secret-display">------</div><input type="text" id="twofa-verify-input" maxlength="6" placeholder="Code" style="text-align:center;letter-spacing:2px;margin-bottom:12px;"><button class="btn btn-success" style="width:100%;" onclick="verify2faSetup()">Activer</button><button class="btn btn-danger" style="width:100%;margin-top:10px;" onclick="closeModal('twofa-setup-modal')">Annuler</button></div></div>
<div id="virement-progress-modal" class="modal">
<div class="modal-content" style="max-width:450px; text-align:center;">
<h3 id="virement-progress-title" style="margin-bottom:16px;">Progression du Virement</h3>
<div id="virement-progress-info" style="margin-bottom:16px; font-size:1rem; color:var(--text-secondary);"></div>
<div class="progress-modern" style="margin: 16px 0; background: var(--bg-body); border-radius: 8px; overflow: hidden; height: 12px; border: 1px solid var(--border);">
<div id="virement-progress-fill" class="progress-fill" style="width: 0%; background: var(--secondary); height: 100%; transition: width 0.5s ease;"></div>
</div>
<div id="virement-progress-percent" style="font-weight: bold; margin-bottom: 16px; font-size:1.2rem;">0%</div>
<div id="virement-progress-input-section" style="display:none;">
<input type="text" id="virement-progress-code" placeholder="Code" style="text-align:center; letter-spacing:2px; margin-bottom:12px; font-size:1.2rem;" inputmode="numeric">
<button id="virement-progress-btn" class="btn btn-primary" style="width:100%;" onclick="nextVirementStep()">Confirmer</button>
</div>
<button id="virement-progress-close" class="btn btn-success" style="width:100%; margin-top:10px; display:none;" onclick="closeVirementProgress()">Terminer</button>
</div>
</div>
<!-- LOCK OVERLAY -->
<div id="session-lock-overlay" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; z-index:9999; background:var(--bg-body);">
<div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); background:var(--bg-card); padding:32px; border-radius:var(--radius-xl); box-shadow:var(--shadow-lg); text-align:center; max-width:380px; width:90%; border:1px solid var(--border);">
<i class="fas fa-shield-alt" style="font-size:3rem; color:var(--secondary); margin-bottom:16px;"></i>
<h3>Session Verrouillée</h3><p style="color:var(--text-muted); margin-bottom:20px;">Code 2FA requis.</p>
<input type="text" id="lock-code-input" maxlength="6" placeholder="000000" style="text-align:center; letter-spacing:4px; font-size:1.5rem; margin-bottom:16px;">
<button class="btn btn-primary" style="width:100%;" onclick="verifyLockCode()">Déverrouiller</button>
<button class="btn btn-dark" style="width:100%; margin-top:10px;" onclick="forceLogout()">Déconnexion</button>
</div>
</div>
<script>
// === ÉTAT GLOBAL & NAV ===
let currentUser = null, tempRegData = null, generatedOTP = null, currentVirementType = 'sepa', selectedGoalId = null;
let balanceChart = null, expenseChart = null, portfolioChart = null, pnlChart = null, priceUpdateInterval = null;
const defaultGoals = [
{id:1, name:'Voyage', icon:'✈️', color:'#3b82f6', target:2000, saved:0, gradient:'linear-gradient(135deg, #3b82f6, #8b5cf6)'},
{id:2, name:'Mariage', icon:'💒', color:'#ec4899', target:15000, saved:0, gradient:'linear-gradient(135deg, #ec4899, #f472b6)'},
{id:3, name:'Voiture', icon:'🚗', color:'#f59e0b', target:10000, saved:0, gradient:'linear-gradient(135deg, #f59e0b, #fbbf24)'},
{id:4, name:'Urgences', icon:'🚑', color:'#ef4444', target:3000, saved:0, gradient:'linear-gradient(135deg, #ef4444, #f87171)'},
{id:5, name:'Études', icon:'🎓', color:'#8b5cf6', target:8000, saved:0, gradient:'linear-gradient(135deg, #8b5cf6, #a78bfa)'},
{id:6, name:'Maison', icon:'🏠', color:'#10b981', target:50000, saved:0, gradient:'linear-gradient(135deg, #10b981, #34d399)'}
];
let cryptoCoins = [{s:'BTC',n:'Bitcoin',p:64230,ch:2.14,cap:1.26e12},{s:'ETH',n:'Ethereum',p:3450,ch:-0.85,cap:415e9},{s:'SOL',n:'Solana',p:145,ch:5.32,cap:65e9},{s:'BNB',n:'BNB',p:580,ch:0.42,cap:88e9},{s:'XRP',n:'Ripple',p:0.62,ch:-1.20,cap:34e9},{s:'DOGE',n:'Dogecoin',p:0.158,ch:4.30,cap:22.7e9},{s:'SHIB',n:'Shiba',p:0.000027,ch:6.80,cap:15.9e9}];
let cryptoPortfolio = JSON.parse(localStorage.getItem('moneo_p')||'{}'), cryptoHistory = JSON.parse(localStorage.getItem('moneo_h')||'[]'), marketFilter = 'all', currentOrderType = 'buy_limit', currentTradingPair = 'BTC';
let pnlHistory = JSON.parse(localStorage.getItem('moneo_pnl')||'{}'), securityState = { enabled: localStorage.getItem('moneo_2fa')==='true', locked: false, lastActivity: Date.now() };
function showPage(p) {
document.querySelectorAll('.page-section').forEach(s=>s.classList.remove('active'));
document.getElementById(p).classList.add('active');
window.scrollTo({top:0});
}
function toggleMobileMenu() {
const menu = document.getElementById('mobile-menu');
const btn = document.getElementById('menu-toggle');
menu.classList.remove('open');
btn.innerHTML = '<i class="fas fa-bars"></i>';
}
function toggleDashView(v) {
['home','cards','credit','savings','crypto'].forEach(x=>document.getElementById('dash-'+x).style.display=x===v?'block':'none');
if(v==='savings')renderGoals();
if(v==='crypto')setTimeout(initCryptoModule,100);
if(v==='cards')renderCards();
if(v==='credit')renderCreditTracking();
}
function openModal(i){document.getElementById(i).style.display='flex';}
function closeModal(i){document.getElementById(i).style.display='none';}
function openSupportModal(){openModal('support-modal');}
// === ASSISTANT IA ===
let aiChatHistory = [];
function openAIChat(){
closeModal('support-modal');
openModal('ai-chat-modal');
if(aiChatHistory.length === 0){
appendAIMessage("bot", "Bonjour ! Je suis l'assistant virtuel Bit Wise. Comment puis-je vous aider aujourd'hui ?");
}
setTimeout(()=>{ const i=document.getElementById('ai-chat-input'); if(i) i.focus(); }, 200);
}
function appendAIMessage(role, text){
const container = document.getElementById('ai-chat-messages');
if(!container) return;
const div = document.createElement('div');
div.className = 'ai-msg ' + (role === 'user' ? 'user' : 'bot');
div.textContent = text;
container.appendChild(div);
container.scrollTop = container.scrollHeight;
}
function showAITyping(){
const container = document.getElementById('ai-chat-messages');
if(!container) return null;
const div = document.createElement('div');
div.className = 'ai-msg bot typing';
div.innerHTML = '<span></span><span></span><span></span>';
div.id = 'ai-typing-indicator';
container.appendChild(div);
container.scrollTop = container.scrollHeight;
return div;
}
async function sendAIChatMessage(){
const input = document.getElementById('ai-chat-input');
const sendBtn = document.querySelector('.ai-chat-send');
const text = (input.value || '').trim();
if(!text) return;
appendAIMessage('user', text);
aiChatHistory.push({role:'user', content:text});
input.value = '';
input.disabled = true;
if(sendBtn) sendBtn.disabled = true;
const typing = showAITyping();
try {
const res = await fetch('/api/chat', {
method: 'POST',
headers: {'Content-Type':'application/json'},
body: JSON.stringify({ messages: aiChatHistory, lang: (window.I18N && window.I18N.current) || localStorage.getItem('moneo_lang') || 'FR' })
});
if(typing) typing.remove();
if(!res.ok) throw new Error('HTTP ' + res.status);
const data = await res.json();
const reply = data.response || "Désolé, je n'ai pas pu générer de réponse.";
aiChatHistory.push({role:'assistant', content: reply});
appendAIMessage('bot', reply);
} catch(err){
if(typing) typing.remove();
appendAIMessage('bot', "Une erreur est survenue. Veuillez réessayer dans un instant ou nous contacter par e-mail.");
} finally {
input.disabled = false;
if(sendBtn) sendBtn.disabled = false;
input.focus();
}
}
function updateClock(){const n=new Date(); if(document.getElementById('dash-clock-time')){document.getElementById('dash-clock-time').innerText=n.toLocaleTimeString('fr-FR'); document.getElementById('dash-clock-date').innerText=n.toLocaleDateString('fr-FR',{weekday:'long',day:'numeric',month:'long'});}}
setInterval(updateClock, 1000);
const themeToggle = document.getElementById('theme-toggle'), html = document.documentElement;
const storedTheme = localStorage.getItem('moneo_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
html.setAttribute('data-theme', storedTheme); updateThemeIcon(storedTheme);
themeToggle.addEventListener('click', () => { const c = html.getAttribute('data-theme'), n = c==='light'?'dark':'light'; html.setAttribute('data-theme', n); localStorage.setItem('moneo_theme', n); updateThemeIcon(n); });
function updateThemeIcon(t){themeToggle.innerHTML=t==='dark'?'<i class="fas fa-sun"></i>':'<i class="fas fa-moon"></i>';}
const menuToggle = document.getElementById('menu-toggle'), mobileMenu = document.getElementById('mobile-menu');
menuToggle.addEventListener('click', () => { mobileMenu.classList.toggle('open'); menuToggle.innerHTML=mobileMenu.classList.contains('open')?'<i class="fas fa-times"></i>':'<i class="fas fa-bars"></i>'; });
document.addEventListener('click', e => { if(!mobileMenu.contains(e.target) && e.target!==menuToggle) { mobileMenu.classList.remove('open'); menuToggle.innerHTML='<i class="fas fa-bars"></i>'; } });
const observer = new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');observer.unobserve(e.target);}}),{threshold:0.1});
document.querySelectorAll('.scroll-animate').forEach(el=>observer.observe(el));
const backToTop = document.getElementById('back-to-top'); window.addEventListener('scroll', ()=>backToTop.classList.toggle('visible', window.scrollY>400)); backToTop.addEventListener('click', ()=>window.scrollTo({top:0,behavior:'smooth'}));
// AUTH & DB
function getUsersDB(){return JSON.parse(localStorage.getItem('moneo_users_db'))||[];}
function saveUsersDB(u){localStorage.setItem('moneo_users_db', JSON.stringify(u));}
// ✅ INSCRIPTION CORRIGÉE & 100% FONCTIONNELLE EN LOCAL
async function handleRegister(e){
e.preventDefault();
const pass=document.getElementById('reg-pass').value, pass2=document.getElementById('reg-pass2').value;
if(pass!==pass2){return showNotification('Erreur','Les mots de passe ne correspondent pas.','error');}
if(pass.length<8){return showNotification('Erreur','Mot de passe trop court (8+ caractères).','error');}
const paysSel=document.getElementById('reg-pays'), pays=paysSel.value, prefix=document.getElementById('reg-phone-prefix').value;
if(!pays){return showNotification('Erreur','Veuillez sélectionner un pays.','error');}
const email=document.getElementById('reg-email').value.trim().toLowerCase();
if(getUsersDB().find(x=>x.email===email)){return showNotification('Erreur','Email existant.','error');}
tempRegData={
nom:document.getElementById('reg-nom').value,
prenom:document.getElementById('reg-prenom').value,
email:email,
pass:pass,
pays:pays,
phonePrefix:prefix,
tel:document.getElementById('reg-tel').value,
address:{
streetNum:document.getElementById('reg-street-num').value,
street:document.getElementById('reg-street').value,
apt:document.getElementById('reg-apt').value,
zip:document.getElementById('reg-zip').value,
city:document.getElementById('reg-city').value
},
idType:document.getElementById('reg-id-type').value,
createdAt:new Date().toISOString(),
iban:'FR76 3000 '+Math.floor(Math.random()*1e10)+' 89',
bic:'MONEFRPPXXX',
solde:1,
cryptoBalance:0,
beneficiaries:[],
transactions:[{desc:"Ouverture",amount:1,date:new Date().toISOString()}],
cards:{virtual:false,physical:false},
goals:JSON.parse(JSON.stringify(defaultGoals))
};
// ✅ Génération OTP côté client (plus besoin d'API backend)
generatedOTP = String(Math.floor(100000 + Math.random() * 900000));
const otpDisplay=document.getElementById('otp-display');
if(otpDisplay) otpDisplay.textContent=generatedOTP;
showNotification('Code généré','Votre code de validation est affiché à l\'écran.','info');
const otpInput=document.getElementById('otp-input');
if(otpInput) otpInput.value='';
openModal('otp-modal');
}
// ✅ VÉRIFICATION OTP CORRIGÉE & 100% FONCTIONNELLE
async function verifyOTP(){
if(!tempRegData){return showNotification('Erreur',"Aucune inscription en attente.",'error');}
const code=document.getElementById('otp-input').value.trim();
if(!code){return showNotification('Erreur','Veuillez saisir le code.','error');}
// Vérification locale
if(code !== generatedOTP){
return showNotification('Erreur','Code incorrect. Réessayez.','error');
}
// Sauvegarde définitive
const u=getUsersDB();
if(u.find(x=>x.email===tempRegData.email)){return showNotification('Erreur','Email existant.','error');}
u.push(tempRegData); saveUsersDB(u);
currentUser=tempRegData;
generatedOTP=null;
const otpDisplay=document.getElementById('otp-display'); if(otpDisplay){otpDisplay.textContent='------';}
closeModal('otp-modal');
setupClientInterface();
renderDashboard();
showPage('dashboard');
showNotification('Bienvenue','Compte activé avec succès.','success');
}
// ✅ CONNEXION CORRIGÉE & 100% FONCTIONNELLE
function handleLogin(e){e.preventDefault(); loginUser(document.getElementById('login-email').value, document.getElementById('login-pass').value);}
function loginUser(mail,pass){
const u=getUsersDB(), em=(mail||'').trim().toLowerCase(), user=u.find(x=>x.email===em&&x.pass===pass);
if(user){
currentUser=user;
localStorage.setItem('moneo_last_user',em);
setupClientInterface();
renderDashboard();
showPage('dashboard');
showNotification('Connexion','Bon retour parmi nous.','success');
}else{
showNotification('Échec','Identifiants incorrects ou compte inexistant.','error');
}
}
function logout(){localStorage.removeItem('moneo_last_user'); location.reload();}
function setupClientInterface(){
document.getElementById('public-nav').style.display='none';
document.getElementById('client-nav').style.display='block';
document.getElementById('auth-btns').style.display='none';
document.querySelectorAll('.client-only').forEach(el=>el.style.display='block');
}
function checkCancellations() {
if (!currentUser || !currentUser.pendingCancellations) return;
const now = Date.now();
let changed = false;
currentUser.pendingCancellations = currentUser.pendingCancellations.filter(c => {
if (now >= c.time) {
currentUser.solde += c.amount;
currentUser.transactions.push({desc: `Annulation Virement ${c.label} → ${c.firstname} ${c.name}`, amount: c.amount, date: new Date().toISOString(), titulaire: `${c.firstname} ${c.name}`, iban: c.iban, bic: c.bic});
changed = true;
return false;
}
return true;
});
if (changed) { saveData(); renderDashboard(); showNotification('Annulation', 'Un transfert a été annulé et recrédité.', 'info'); }
}
setInterval(checkCancellations, 5000);
// ✅ RESTAURATION DE SESSION AU CHARGEMENT
window.addEventListener('load',()=>{
const last=localStorage.getItem('moneo_last_user');
if(last){
const u=getUsersDB(), user=u.find(x=>x.email===last);
if(user){currentUser=user; setupClientInterface(); renderDashboard(); showPage('dashboard');}
}
setTimeout(()=>document.getElementById('loading-screen').classList.add('hidden'),800);
});
// DASHBOARD & CHARTS
function renderDashboard(){
if(!currentUser)return;
const un=document.getElementById('dash-user-name'); if(un)un.innerText=currentUser.prenom+' '+currentUser.nom;
document.getElementById('dash-solde').innerText=currentUser.solde.toFixed(2)+' €';
document.getElementById('dash-iban').innerText=currentUser.iban;
const bicEl=document.getElementById('dash-bic'); if(bicEl){bicEl.innerText='BIC: '+(currentUser.bic||'MONEFRPPXXX');}
const hist=document.getElementById('trans-history'); hist.innerHTML='';
(currentUser.transactions||[]).slice().reverse().forEach(t=>{
const dateObj = new Date(t.date); const dateStr = dateObj.toLocaleDateString('fr-FR'); const timeStr = dateObj.toLocaleTimeString('fr-FR');
const titulaire = t.titulaire || (t.amount < 0 ? 'Bénéficiaire' : (currentUser.prenom + ' ' + currentUser.nom));
const iban = t.iban || (t.amount < 0 ? 'Non spécifié' : currentUser.iban); const bic = t.bic || (t.amount < 0 ? 'Non spécifié' : (currentUser.bic || 'MONEFRPPXXX'));
hist.innerHTML+=`<div class="t-item" style="cursor:pointer;flex-direction:column;" onclick="const d=this.querySelector('.t-details'); d.style.display=d.style.display==='none'?'block':'none';">
<div style="display:flex;justify-content:space-between;width:100%;"><span>${t.desc}</span><span class="${t.amount>=0?'t-plus':'t-minus'}">${t.amount>=0?'+':''}${t.amount.toFixed(2)} €</span></div>
<div class="t-details" style="display:none;margin-top:12px;padding-top:12px;border-top:1px solid var(--border);font-size:0.9rem;color:var(--text-secondary);">
<div style="margin-bottom:6px;"><strong>Titulaire de compte :</strong> ${titulaire}</div><div style="margin-bottom:6px;"><strong>IBAN :</strong> ${iban}</div>
<div style="margin-bottom:6px;"><strong>BIC/SWIFT :</strong> ${bic}</div><div style="margin-bottom:6px;"><strong>Montant :</strong> ${t.amount>=0?'+':''}${t.amount.toFixed(2)} €</div>
<div><strong>Heure :</strong> ${dateStr} à ${timeStr}</div></div></div>`;
});
renderGoals(); renderBalanceChart(); renderExpenseChart();
}
function getChartColors(){const d=html.getAttribute('data-theme')==='dark'; return{text:d?'#cbd5e1':'#475569',grid:d?'rgba(255,255,255,0.1)':'rgba(0,0,0,0.06)',line:'#3b82f6'};}
function renderBalanceChart(){const ctx=document.getElementById('balanceChart'); if(!ctx)return; const labels=[], data=[], base=(currentUser&&typeof currentUser.solde==='number')?currentUser.solde:0; for(let i=0;i<30;i++){labels.push(i+'j'); data.push(base);} if(balanceChart)balanceChart.destroy(); balanceChart=new Chart(ctx,{type:'line',data:{labels,datasets:[{data,borderColor:'#3b82f6',tension:0.4,fill:true,backgroundColor:'rgba(59,130,246,0.1)'}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{display:false},y:{display:false}}}});}
function renderExpenseChart(){const ctx=document.getElementById('expenseChart'); if(!ctx)return; if(expenseChart)expenseChart.destroy(); expenseChart=new Chart(ctx,{type:'doughnut',data:{labels:['Alim','Transport','Loisirs','Santé','Autres'],datasets:[{data:[400,200,150,100,50],borderWidth:0}]},options:{responsive:true,maintainAspectRatio:false,cutout:'65%',plugins:{legend:{position:'bottom'}}}}); }
// CRÉDIT
function calcLoanRealTime() {
const amountEl = document.getElementById('loan-amount');
const monthsEl = document.getElementById('loan-duration');
const rateEl = document.getElementById('loan-rate');
if (!amountEl || !monthsEl || !rateEl) return;
const amount = Number(amountEl.value) || 0;
const months = parseInt(monthsEl.value) || 60;
const rate = rateEl.value !== '' ? Number(rateEl.value) : 3.0;
let monthlyPayment = 0;
if (amount > 0 && months > 0) {
const monthlyRate = (rate / 100) / 12;
monthlyPayment = monthlyRate === 0 ? amount / months : (amount * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -months));
}
const insurance = (amount * 0.0036) / 12;
const totalMonthly = monthlyPayment + insurance;
document.getElementById('loan-monthly').innerText = monthlyPayment.toFixed(2) + ' €';
document.getElementById('loan-insurance').innerText = insurance.toFixed(2) + ' €';
document.getElementById('loan-total-monthly').innerText = totalMonthly.toFixed(2) + ' €';
const debtRatio = (totalMonthly / 2500) * 100;
document.getElementById('debt-ratio-value').innerText = debtRatio.toFixed(1) + '%';
const ratioFill = document.getElementById('debt-ratio-fill');
const ratioStatus = document.getElementById('debt-ratio-status');
const applyBtn = document.getElementById('btn-apply-loan');
ratioFill.style.width = Math.min(debtRatio, 100) + '%'; ratioFill.className = 'ratio-fill';
if (debtRatio <= 35) { ratioFill.style.background = 'var(--accent)'; ratioStatus.innerHTML = '<i class="fas fa-check-circle" style="color:var(--accent)"></i> Éligibilité: Favorable'; applyBtn.disabled = false; }
else if (debtRatio <= 40) { ratioFill.style.background = 'var(--warning)'; ratioStatus.innerHTML = '<i class="fas fa-exclamation-triangle" style="color:var(--warning)"></i> Éligibilité: À l\'étude'; applyBtn.disabled = false; }
else { ratioFill.style.background = 'var(--danger)'; ratioStatus.innerHTML = '<i class="fas fa-times-circle" style="color:var(--danger)"></i> Éligibilité: Défavorable'; applyBtn.disabled = true; }
if (currentUser && currentUser.loanApplication) { applyBtn.disabled = true; applyBtn.innerText = "Demande déjà en cours"; } else { applyBtn.innerText = "Demander un crédit"; }
}
let creditUpdateInterval = null;
// ✅ VERSION SÉCURISÉE : Validation stricte des champs obligatoires avant soumission
function applyLoan(){
const amountEl = document.getElementById('loan-amount');
const durationEl = document.getElementById('loan-duration');
const proofEl = document.getElementById('loan-income-proof');
const docEl = document.getElementById('loan-document');
const amount = parseFloat(amountEl?.value);
const duration = durationEl?.value;
const proofType = proofEl?.value;
const hasFile = docEl?.files?.length > 0;
if (!amount || amount <= 0) return showNotification('Montant requis', 'Veuillez saisir un montant valide.', 'error');
if (!duration) return showNotification('Durée requise', 'Veuillez sélectionner une durée de remboursement.', 'error');
if (!proofType) return showNotification('Justificatif requis', 'Veuillez choisir un type de justificatif de revenu.', 'error');
if (!hasFile) return showNotification('Document requis', 'Veuillez télécharger votre justificatif avant de continuer.', 'error');
// ✅ SI TOUT EST VALIDÉ → Création de la demande
currentUser.loanApplication = { amount: amount, startTime: Date.now(), accountNumber: Math.floor(10000000 + Math.random() * 90000000).toString(), state: 'tracking', progress: 0, contractSigned: false, insuranceSigned: false, transferStarted: false, transferProgress: 0, completed: false };
if (!currentUser.creditHistory) currentUser.creditHistory = [];
currentUser.creditHistory.push(currentUser.loanApplication);
saveData(); showNotification('Demande envoyée','Analyse en cours...','info'); renderCreditTracking();
}
function animateCreditScore() {
const svg = document.getElementById('score-circle-svg'); const progress = document.getElementById('score-circle-progress'); const scoreValue = document.getElementById('score-value'); const badge = document.getElementById('eligibility-badge');
if(!svg || !progress || !scoreValue) return;
progress.style.transition = 'none'; progress.style.strokeDashoffset = '339.292'; progress.setAttribute('stroke', 'var(--text-muted)'); scoreValue.textContent = '0'; badge.style.display = 'none'; svg.classList.add('circle-spin-anim');
setTimeout(() => {
svg.classList.remove('circle-spin-anim'); svg.style.transform = 'rotate(-90deg)';
const targetScore = 530; const maxScore = 850; const circumference = 339.292; const offset = circumference - (targetScore / maxScore) * circumference;
progress.style.transition = 'stroke-dashoffset 2s ease-out, stroke 0.5s ease-in-out'; progress.style.strokeDashoffset = offset;
let currentScore = 0; const duration = 2000; const startTime = performance.now();
function updateCounter(time) {
const elapsed = time - startTime; const progressRatio = Math.min(elapsed / duration, 1); const easeProgress = 1 - (1 - progressRatio) * (1 - progressRatio);
currentScore = Math.floor(easeProgress * targetScore); scoreValue.textContent = currentScore;
if (progressRatio < 1) { requestAnimationFrame(updateCounter); } else {
scoreValue.textContent = targetScore; progress.setAttribute('stroke', 'var(--secondary)');
badge.className = 'badge info'; badge.style.backgroundColor = 'rgba(59, 130, 246, 0.1)'; badge.style.color = 'var(--secondary)'; badge.textContent = 'Éligibilité conditionnelle'; badge.style.display = 'inline-block';
}
} requestAnimationFrame(updateCounter);
}, 1500);
}
function renderCreditHistory() {
const histContainer = document.getElementById('credit-history-list'); const statusTextContainer = document.getElementById('credit-status-text');
if (!histContainer) return;
let history = []; if (currentUser.creditHistory && currentUser.creditHistory.length > 0) { history = currentUser.creditHistory; } else if (currentUser.loanApplication) { history = [currentUser.loanApplication]; }
let hasActiveRequest = false;
if (history.length === 0) { histContainer.innerHTML = '<p style="color: var(--text-muted); font-style: italic;">Aucune demande de crédit.</p>'; if (statusTextContainer) statusTextContainer.innerHTML = '<p style="color: var(--text-muted); font-weight: 500;">Aucune demande en cours.</p>'; return; }
histContainer.innerHTML = '';
history.forEach((app, idx) => {
const date = new Date(app.startTime).toLocaleDateString('fr-FR');
let statusText = "En cours d'étude", statusColor = "var(--warning)";
if (app.state === 'completed') { statusText = "Approuvé et débloqué"; statusColor = "var(--success)"; } else if (app.contractSigned || app.state === 'transferring') { statusText = "En cours de déblocage"; statusColor = "var(--info)"; hasActiveRequest = true; } else { hasActiveRequest = true; }
histContainer.innerHTML += `<div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid var(--border);"><div><strong>Demande N°${app.accountNumber || '---'}</strong><br><span style="color: var(--text-muted); font-size: 0.8rem;">${date}</span></div><div style="text-align: right;"><strong>${app.amount.toFixed(2)} €</strong><br><span class="badge" style="background: ${statusColor}; color: white; font-size: 0.7rem; padding: 2px 6px;">${statusText}</span></div></div>`;
});
if (statusTextContainer) { statusTextContainer.innerHTML = hasActiveRequest ? '<p style="color: var(--secondary); font-weight: 500;">Il y a une demande de crédit en cours.</p>' : '<p style="color: var(--text-muted); font-weight: 500;">Aucune demande en cours.</p>'; }
}
function renderCreditTracking() {
if (!currentUser) return; renderCreditHistory();
if (!currentUser.loanApplication) {
document.getElementById('credit-scoring-section').style.display = 'block'; document.getElementById('credit-form-section').style.display = 'block';
const trackSec = document.getElementById('credit-tracking-section'); if(trackSec) trackSec.style.display = 'none';
if(!window._creditScoreAnimated) { animateCreditScore(); window._creditScoreAnimated = true; }
calcLoanRealTime(); return;
}
window._creditScoreAnimated = false;
document.getElementById('credit-scoring-section').style.display = 'none'; document.getElementById('credit-form-section').style.display = 'block'; document.getElementById('credit-tracking-section').style.display = 'block';
calcLoanRealTime(); updateCreditState(); if (creditUpdateInterval) clearInterval(creditUpdateInterval); creditUpdateInterval = setInterval(updateCreditState, 1000);
}
function updateCreditState() {
if (!currentUser || !currentUser.loanApplication) return;
const app = currentUser.loanApplication;
if (app.state === 'tracking') {
const elapsedMins = (Date.now() - app.startTime) / 60000;
let pct = elapsedMins < 0.1 ? 0 : elapsedMins < 0.3 ? 12 : elapsedMins < 3.3 ? 23 : elapsedMins < 5.3 ? 31 : elapsedMins < 11.3 ? 44 : elapsedMins < 15.3 ? 69 : elapsedMins < 22.3 ? 78 : elapsedMins < 202.3 ? 84 : elapsedMins < 442.3 ? 89 : elapsedMins < 622.3 ? 95 : 100;
app.progress = pct; saveData();
document.getElementById('credit-tracking-pct').innerText = pct + '%'; document.getElementById('credit-tracking-bar').style.width = pct + '%';
if (pct >= 100) { app.state = 'blocked'; saveData(); }
}
if (app.state === 'blocked' || app.state === 'contract_signed' || app.state === 'transferring' || app.state === 'completed') {
document.getElementById('credit-tracking-progress-container').style.display = 'none'; document.getElementById('credit-validation-message').style.display = 'block';
document.getElementById('credit-amount-display').innerText = app.amount.toFixed(2); document.getElementById('credit-account-number').innerText = app.accountNumber;
if (app.state === 'blocked') { document.getElementById('credit-contract-section').style.display = 'block'; document.getElementById('credit-unblocked-section').style.display = 'none'; }
else { document.getElementById('credit-contract-section').style.display = 'none'; if (app.state === 'contract_signed') { document.getElementById('credit-unblocked-section').style.display = 'block'; } else { document.getElementById('credit-unblocked-section').style.display = 'none'; } }
}
if (app.state === 'transferring' || app.state === 'completed') {
document.getElementById('credit-transfer-section').style.display = 'block'; document.getElementById('credit-validation-message').style.display = 'none'; document.getElementById('credit-unblocked-section').style.display = 'none';
if (!app.transferProgress) app.transferProgress = 0;
if (app.transferProgress < 37 && !app.insuranceSigned) { app.transferProgress += 1.5; if (app.transferProgress > 37) app.transferProgress = 37; } else if (app.insuranceSigned && app.transferProgress < 100) { app.transferProgress += 2; if (app.transferProgress > 100) app.transferProgress = 100; }
document.getElementById('credit-transfer-pct').innerText = Math.floor(app.transferProgress) + '%'; document.getElementById('credit-transfer-bar').style.width = app.transferProgress + '%';
if (app.transferProgress === 37 && !app.insuranceSigned) { document.getElementById('credit-insurance-section').style.display = 'block'; } else { document.getElementById('credit-insurance-section').style.display = 'none'; }
if (app.transferProgress === 100 && app.state !== 'completed') {
app.state = 'completed'; currentUser.solde += app.amount;
currentUser.transactions.push({ desc: `Crédit validé N°${app.accountNumber}`, amount: app.amount, date: new Date().toISOString(), titulaire: 'Bit Wise Bank (Crédit)', iban: 'MONEFRPPXXX' });
saveData(); renderDashboard();
}
if (app.state === 'completed') { document.getElementById('credit-transfer-section').style.display = 'none'; document.getElementById('credit-final-success').style.display = 'block'; }
}
}
function signCreditContract() { const code = document.getElementById('credit-contract-code').value.trim(); if (!code) return showNotification('Erreur', 'Code requis.', 'error'); currentUser.loanApplication.state = 'contract_signed'; currentUser.loanApplication.contractSigned = true; saveData(); showNotification('Succès', 'Contrat signé. Fonds débloqués.', 'success'); updateCreditState(); }
function startMainTransfer() { currentUser.loanApplication.state = 'transferring'; currentUser.loanApplication.transferStarted = true; saveData(); updateCreditState(); }
function signInsuranceContract() { const code = document.getElementById('credit-insurance-code').value.trim(); if (!code) return showNotification('Erreur', 'Code requis.', 'error'); currentUser.loanApplication.insuranceSigned = true; saveData(); showNotification('Succès', 'Assurance signée. Transfert en cours.', 'success'); updateCreditState(); }
function devFastForward() { if (currentUser && currentUser.loanApplication) { currentUser.loanApplication.startTime -= 60 * 60000; saveData(); updateCreditState(); } }
// ÉPARGNE & OBJECTIFS
function renderGoals(){const c=document.getElementById('goals-container'); c.innerHTML=''; let tot=0; currentUser.goals.forEach(g=>{tot+=g.saved; const p=Math.min(100,(g.saved/g.target)*100); c.innerHTML+=`<div class="card goal-card scroll-animate" style="--goal-gradient:${g.gradient}"><div class="goal-icon-wrapper" style="background:${g.gradient}">${g.icon}</div><h4>${g.name}</h4><p>${g.saved.toFixed(0)}€ / ${g.target.toLocaleString('fr-FR')}€</p><div class="goal-progress-bar"><div class="goal-progress-fill" style="width:${p}%;background:${g.gradient}"></div></div>${p>=100?'<div class="goal-reached-badge"><i class="fas fa-trophy"></i> Atteint</div>':''}<div class="goal-actions"><button class="btn btn-success" onclick="openGoalActionModal(${g.id},'deposit')" ${currentUser.solde<=0?'disabled':''}><i class="fas fa-arrow-down"></i></button><button class="btn btn-dark" onclick="openGoalActionModal(${g.id},'withdraw')" ${g.saved<=0?'disabled':''}><i class="fas fa-arrow-up"></i></button></div></div>`;}); document.getElementById('total-savings-display').innerText=tot.toFixed(2)+' €'; document.querySelectorAll('#goals-container .goal-card').forEach(el=>observer.observe(el));}
function openGoalActionModal(id,action){selectedGoalId=id; const g=currentUser.goals.find(x=>x.id===id); document.getElementById('goal-action-title').innerText=action==='deposit'?`Dépôt vers ${g.icon} ${g.name}`:`Retrait ${g.icon} ${g.name}`; document.getElementById('goal-action-balance-info').innerHTML=action==='deposit'?`Solde dispo: <strong>${currentUser.solde.toFixed(2)} €</strong>`:`Solde objectif: <strong>${g.saved.toFixed(2)} €</strong>`; document.getElementById('goal-action-amount').max=action==='deposit'?currentUser.solde:g.saved; document.getElementById('goal-action-confirm').onclick=()=>confirmGoalAction(action); openModal('goal-action-modal');}
function confirmGoalAction(action){const a=parseFloat(document.getElementById('goal-action-amount').value), g=currentUser.goals.find(x=>x.id===selectedGoalId); if(!a||a<=0)return showNotification('Erreur','Montant invalide.','error'); if(action==='deposit'&&a>currentUser.solde)return showNotification('Erreur','Solde insuffisant.','error'); if(action==='withdraw'&&a>g.saved)return showNotification('Erreur','Solde objectif insuffisant.','error'); if(action==='deposit'){currentUser.solde-=a; g.saved+=a;}else{g.saved-=a; currentUser.solde+=a;} saveData(); renderDashboard(); closeModal('goal-action-modal'); showNotification('✅ Effectué',`${action==='deposit'?'Dépôt':'Retrait'} de ${a.toFixed(2)} €.`,'success');}
function saveData(){if(!currentUser)return; const u=getUsersDB(), i=u.findIndex(x=>x.email===currentUser.email); if(i!==-1){u[i]=currentUser; saveUsersDB(u);}}
function openAddBeneficiaryModal(){['new-ben-name-dash','new-ben-firstname-dash','new-ben-iban-dash','new-ben-bic-dash'].forEach(id=>{const el=document.getElementById(id); if(el) el.value='';}); openModal('add-beneficiary-modal');}
function saveNewBeneficiary(){
const name=document.getElementById('new-ben-name-dash').value.trim(); const firstname=document.getElementById('new-ben-firstname-dash').value.trim();
const iban=document.getElementById('new-ben-iban-dash').value.trim(); const bic=document.getElementById('new-ben-bic-dash').value.trim();
if(!name||!firstname||!iban||!bic){return showNotification('Erreur','Nom, Prénom, IBAN et BIC/Swift requis.','error');}
if(!Array.isArray(currentUser.beneficiaries)) currentUser.beneficiaries=[];
currentUser.beneficiaries.push({name,firstname,iban,bic}); saveData(); closeModal('add-beneficiary-modal'); showNotification('✅','Bénéficiaire enregistré.','success');
}
function populateBeneficiarySelect(){const sel=document.getElementById('virement-beneficiary'); if(!sel) return; const list=(currentUser&&Array.isArray(currentUser.beneficiaries))?currentUser.beneficiaries:[]; sel.innerHTML='<option value="">Choisir un bénéficiaire...</option>'+list.map((b,i)=>`<option value="${i}">${b.firstname||''} ${b.name||''} — ${b.iban||''}</option>`).join('');}
function applyBeneficiarySelection(){const sel=document.getElementById('virement-beneficiary'); if(!sel) return; const i=sel.value; if(i===''||!currentUser||!currentUser.beneficiaries) return; const b=currentUser.beneficiaries[parseInt(i,10)]; if(!b) return; document.getElementById('virement-name-manual').value=b.name||''; document.getElementById('virement-firstname-manual').value=b.firstname||''; document.getElementById('virement-iban-manual').value=b.iban||''; document.getElementById('virement-bic-manual').value=b.bic||'';}
function openVirementModal(t){
currentVirementType=t; const title=document.getElementById('virement-title'); if(title) title.innerText=t==='instant'?'Virement Instantané':'Virement SEPA';
['virement-name-manual','virement-firstname-manual','virement-iban-manual','virement-bic-manual','virement-amount'].forEach(id=>{const el=document.getElementById(id); if(el) el.value='';});
populateBeneficiarySelect(); const sel=document.getElementById('virement-beneficiary'); if(sel) sel.value=''; openModal('virement-modal');
}
let virementState = {};
function startSecureTransfer(){
const amountEl = document.getElementById('virement-amount');
const nameEl = document.getElementById('virement-name-manual');
const firstnameEl = document.getElementById('virement-firstname-manual');
const ibanEl = document.getElementById('virement-iban-manual');
const bicEl = document.getElementById('virement-bic-manual');
if (!amountEl || !nameEl || !firstnameEl || !ibanEl || !bicEl) return;
const a = Number(amountEl.value);
const name = nameEl.value.trim(); const firstname = firstnameEl.value.trim();
const iban = ibanEl.value.trim(); const bic = bicEl.value.trim();
if(!name||!firstname||!iban||!bic) return showNotification('Erreur','Nom, Prénom, IBAN et BIC/Swift requis.','error');
if(!Number.isFinite(a) || a<=0 || a>currentUser.solde) return showNotification('Erreur','Montant invalide.','error');
virementState = { step: 1, amount: a, name, firstname, iban, bic, type: currentVirementType };
closeModal('virement-modal'); document.getElementById('virement-progress-fill').style.width = '0%'; document.getElementById('virement-progress-percent').innerText = '0%';
document.getElementById('virement-progress-input-section').style.display = 'none'; document.getElementById('virement-progress-close').style.display = 'none';
document.getElementById('virement-progress-info').innerHTML = `Initialisation du transfert...`; openModal('virement-progress-modal');
animateProgress(0, 87, 2000, () => {
document.getElementById('virement-progress-info').innerHTML = `Saisissez le code pour : <strong>${firstname} ${name}</strong>.`;
document.getElementById('virement-progress-input-section').style.display = 'block'; document.getElementById('virement-progress-code').value = '';
});
}
function animateProgress(start, end, duration, callback) { let current = start; const intervalTime = 50; const steps = duration / intervalTime; const increment = (end - start) / steps; const timer = setInterval(() => { current += increment; if(current >= end) { current = end; clearInterval(timer); if(callback) callback(); } document.getElementById('virement-progress-fill').style.width = current + '%'; document.getElementById('virement-progress-percent').innerText = Math.floor(current) + '%'; }, intervalTime); }
function nextVirementStep() {
const code = document.getElementById('virement-progress-code').value.trim();
if(!code) return showNotification('Erreur', 'Code requis.', 'error');
document.getElementById('virement-progress-input-section').style.display = 'none';
if(virementState.step === 1) { virementState.step = 2; animateProgress(87, 91, 1500, () => { document.getElementById('virement-progress-info').innerHTML = `Validation finale pour : <strong>${virementState.iban}</strong>.`; document.getElementById('virement-progress-input-section').style.display = 'block'; document.getElementById('virement-progress-code').value = ''; }); }
else if(virementState.step === 2) { virementState.step = 3; document.getElementById('virement-progress-info').innerHTML = `Traitement en cours (~1 min)...`; animateProgress(91, 98, 60000, () => { document.getElementById('virement-progress-info').innerHTML = `Finalisation pour : <strong>${virementState.firstname} ${virementState.name}</strong>.`; document.getElementById('virement-progress-input-section').style.display = 'block'; document.getElementById('virement-progress-code').value = ''; }); }
else if(virementState.step === 3) {
virementState.step = 4; animateProgress(98, 100, 1000, () => {
document.getElementById('virement-progress-info').innerHTML = `<strong style="color:var(--accent);">Transfert réussi !</strong>`; document.getElementById('virement-progress-close').style.display = 'block';
currentUser.solde -= virementState.amount; const label = virementState.type === 'instant' ? 'Instantané' : 'SEPA';
currentUser.transactions.push({ desc: `Virement ${label} → ${virementState.firstname} ${virementState.name}`, amount: -virementState.amount, date: new Date().toISOString(), titulaire: `${virementState.firstname} ${virementState.name}`, iban: virementState.iban, bic: virementState.bic });
currentUser.pendingCancellations = currentUser.pendingCancellations || []; currentUser.pendingCancellations.push({ amount: virementState.amount, firstname: virementState.firstname, name: virementState.name, label: label, time: Date.now() + 600000, iban: virementState.iban, bic: virementState.bic });
saveData(); renderDashboard();
});
}
}
function closeVirementProgress() { closeModal('virement-progress-modal'); }
function renderCards() {
const c = document.getElementById('cards-container'); if (!c || !currentUser) return; c.innerHTML = '';
if (!currentUser.cards) currentUser.cards = { virtual: null, physical: null };
['virtual', 'physical'].forEach(t => {
const cd = currentUser.cards[t], phys = t==='physical', pr = phys?28:17; const title = phys?'Carte Physique':'Carte Virtuelle';
if(!cd){ c.innerHTML+=`<div class="card"><h3>${title}</h3><button class="btn btn-primary" style="width:100%;" onclick="startBuyCard('${t}',${pr})">Acheter (${pr}€)</button></div>`; }
else {
const fz=cd.frozen?'❄️ Dégeler':'❄️ Geler', cl=cd.frozen?'btn-success':'btn-warning';
c.innerHTML+=`<div class="card"><h3>${title}</h3><div class="visa-real" style="${fz?'opacity:0.6;':''} cursor:pointer;" onclick="promptCardPin('${t}')"><div style="display:flex;justify-content:space-between;"><div class="chip"></div><i class="fab fa-cc-visa" style="font-size:2.5rem;"></i></div><div style="font-family:monospace;font-size:1.2rem;letter-spacing:2px;">**** **** **** ****</div><div style="display:flex;justify-content:space-between;"><div class="card-holder-name">${currentUser.prenom} ${currentUser.nom}</div><div>**/**</div></div></div><div style="margin-top:12px;display:flex;flex-direction:column;gap:8px;"><button class="btn btn-dark" style="width:100%;" onclick="openLimitModal('${t}')">📏 Plafond (${cd.limit}€)</button><button class="btn ${cl}" style="width:100%;" onclick="toggleFreezeCard('${t}')">${fz}</button><button class="btn btn-danger" style="width:100%;" onclick="reportLostCard('${t}')">🚨 Perte</button></div></div>`;
}
});
}
let activeCardAction=null,activeCardType=null,activeCardPrice=null;
function startBuyCard(t,p){if(currentUser.solde<p)return showNotification('Erreur','Solde insuffisant.','error');activeCardAction='buy';activeCardType=t;activeCardPrice=p;document.getElementById('card-pin-title').innerText='Code PIN carte';document.getElementById('card-pin-input').value='';openModal('card-pin-modal');}
function promptCardPin(t){if(currentUser.cards[t]?.frozen)return showNotification('Info','Carte gelée.','warning');activeCardAction='view';activeCardType=t;document.getElementById('card-pin-title').innerText='Code PIN';document.getElementById('card-pin-input').value='';openModal('card-pin-modal');}
function confirmCardPin(){
const pin=document.getElementById('card-pin-input').value;
if(!/^\d{4}$/.test(pin)) return showNotification('Erreur','4 chiffres.','error');
if(activeCardAction==='buy'){
currentUser.solde-=activeCardPrice; currentUser.transactions.push({desc:`Carte ${activeCardType}`,amount:-activeCardPrice,date:new Date().toISOString(),titulaire:'Bit Wise'});
currentUser.cards[activeCardType]={pin,limit:1000,frozen:false,status:activeCardType==='physical'?'shipping':'active',pan:'45'+Math.floor(Math.random()*1e16),cvv:Math.floor(100+Math.random()*900),exp:'12/28'};
saveData(); renderDashboard(); renderCards(); closeModal('card-pin-modal'); showNotification('✅','Carte activée.','success');
} else if(activeCardAction==='view'){
const cd=currentUser.cards[activeCardType]; if(cd.pin!==pin) return showNotification('Erreur','Code incorrect.','error');
closeModal('card-pin-modal'); document.getElementById('card-view-pan').innerText=cd.pan.replace(/(.{4})/g,'$1 ').trim(); document.getElementById('card-view-cvv').innerText=cd.cvv; document.getElementById('card-view-exp').innerText=cd.exp; openModal('card-view-modal');
}
}
function openLimitModal(t){activeCardType=t;document.getElementById('card-limit-input').value=currentUser.cards[t].limit;document.getElementById('card-limit-display').innerText=currentUser.cards[t].limit+' €';openModal('card-limit-modal');}
function updateLimitDisplay(){document.getElementById('card-limit-display').innerText=document.getElementById('card-limit-input').value+' €';}
function confirmCardLimit(){currentUser.cards[activeCardType].limit=parseInt(document.getElementById('card-limit-input').value,10);saveData();renderCards();closeModal('card-limit-modal');showNotification('✅','Plafond mis à jour.','success');}
function toggleFreezeCard(t){currentUser.cards[t].frozen=!currentUser.cards[t].frozen;saveData();renderCards();showNotification('ℹ️',currentUser.cards[t].frozen?'Carte gelée.':'Carte dégelée.','info');}
function reportLostCard(t){if(!confirm('Signaler perte ?'))return;currentUser.cards[t]=null;saveData();renderCards();showNotification('🚨','Carte bloquée.','warning');}
// COUNTRIES & ADDRESS
const COUNTRIES=[{n:"Afghanistan",c:"+93"},{n:"France",c:"+33"},{n:"États-Unis",c:"+1"},{n:"Allemagne",c:"+49"},{n:"Espagne",c:"+34"},{n:"Italie",c:"+39"},{n:"Royaume-Uni",c:"+44"},{n:"Canada",c:"+1"},{n:"Japon",c:"+81"},{n:"Chine",c:"+86"},{n:"Brésil",c:"+55"},{n:"Maroc",c:"+212"},{n:"Algérie",c:"+213"},{n:"Tunisie",c:"+216"},{n:"Sénégal",c:"+221"},{n:"Côte d'Ivoire",c:"+225"},{n:"Cameroun",c:"+237"},{n:"Belgique",c:"+32"},{n:"Suisse",c:"+41"},{n:"Portugal",c:"+351"},{n:"Pologne",c:"+48"},{n:"Russie",c:"+7"},{n:"Inde",c:"+91"},{n:"Australie",c:"+61"},{n:"Mexique",c:"+52"}];
function populateCountrySelect(sel,prefSel,def){if(!sel)return;sel.innerHTML='<option value="" disabled>Pays</option>'+COUNTRIES.map(c=>`<option value="${c.n}"${c.n===def?' selected':''}>${c.n}</option>`).join('');if(prefSel)prefSel.innerHTML=COUNTRIES.map(c=>`<option value="${c.c}"${c.n===def?' selected':''}>${c.n} (${c.c})</option>`).join('');}
function updatePhonePrefix(){const sel=document.getElementById('reg-pays'),pref=document.getElementById('reg-phone-prefix');const o=sel.options[sel.selectedIndex];if(o)pref.value=COUNTRIES.find(c=>c.n===o.value)?.c||pref.value;}
function updateProfilePhonePrefix(){updatePhonePrefix();}
document.addEventListener('DOMContentLoaded',()=>{populateCountrySelect(document.getElementById('reg-pays'),document.getElementById('reg-phone-prefix'),'France');populateCountrySelect(document.getElementById('prof-pays'),document.getElementById('prof-phone-prefix'),'France');});
let _addrTimer=null;function toggleManualAddress(){document.getElementById('reg-address-search').value='';document.getElementById('address-suggestions').style.display='none';}function simulateAddressAutoComplete(){const q=document.getElementById('reg-address-search').value.trim(),box=document.getElementById('address-suggestions');clearTimeout(_addrTimer);if(q.length<3){box.style.display='none';return;}_addrTimer=setTimeout(()=>{const s=[{n:"12",s:"Rue Paix",z:"75002",c:"Paris"},{n:"45",s:"Av Champs",z:"75008",c:"Paris"}];box.innerHTML=s.map((x,i)=>`<div class="addr-sugg" style="padding:8px;cursor:pointer;border-bottom:1px solid var(--border);" onclick="document.getElementById('reg-street-num').value='${x.n}';document.getElementById('reg-street').value='${x.s}';document.getElementById('reg-zip').value='${x.z}';document.getElementById('reg-city').value='${x.c}';document.getElementById('address-suggestions').style.display='none';">${x.n} ${x.s}, ${x.z} ${x.c}</div>`).join('');box.style.display='block';},250);}
function renderProfile(){if(!currentUser){showPage('login');return;}populateCountrySelect(document.getElementById('prof-pays'),document.getElementById('prof-phone-prefix'),currentUser.pays||'France');document.getElementById('prof-nom').value=currentUser.nom||'';document.getElementById('prof-prenom').value=currentUser.prenom||'';document.getElementById('prof-email').value=currentUser.email||'';document.getElementById('prof-tel').value=currentUser.tel||'';const a=currentUser.address||{};document.getElementById('prof-street-num').value=a.streetNum||'';document.getElementById('prof-street').value=a.street||'';document.getElementById('prof-apt').value=a.apt||'';document.getElementById('prof-zip').value=a.zip||'';document.getElementById('prof-city').value=a.city||'';}
function handleProfileSave(e){e.preventDefault();if(!currentUser)return;currentUser.nom=document.getElementById('prof-nom').value;currentUser.prenom=document.getElementById('prof-prenom').value;currentUser.email=document.getElementById('prof-email').value.trim().toLowerCase();currentUser.pays=document.getElementById('prof-pays').value;currentUser.phonePrefix=document.getElementById('prof-phone-prefix').value;currentUser.tel=document.getElementById('prof-tel').value;currentUser.address={streetNum:document.getElementById('prof-street-num').value,street:document.getElementById('prof-street').value,apt:document.getElementById('prof-apt').value,zip:document.getElementById('prof-zip').value,city:document.getElementById('prof-city').value};saveData();renderDashboard();localStorage.setItem('moneo_last_user',currentUser.email);showNotification('✅','Enregistré.','success');}
function showNotification(title,msg,type='info',dur=4000){const c=document.getElementById('toast-container'),icons={info:'fa-bell',success:'fa-check-circle',warning:'fa-exclamation-triangle',error:'fa-times-circle'},t=document.createElement('div');t.className=`toast ${type}`;t.innerHTML=`<i class="fas ${icons[type]} toast-icon"></i><div class="toast-content"><div class="toast-title">${title}</div><div class="toast-message">${msg}</div></div><i class="fas fa-times toast-close" onclick="this.parentElement.remove()"></i>`;c.appendChild(t);setTimeout(()=>{if(t.parentElement)t.remove();},dur);}
// CRYPTO & TRADING MODULE
function initCryptoModule(){updatePrices(); renderMarkets(); renderWatchlist(); renderPortfolio(); renderOrderBook(); renderPnl(); initFloatingWidget();}
function updatePrices(){cryptoCoins.forEach(c=>{c.p*=(1+(Math.random()-0.48)*0.002); c.ch=parseFloat((c.ch+(Math.random()-0.48)*0.5).toFixed(2));}); renderMarkets(); updatePnl(); updateWidgetPrices();}
const fmtUSD=v=>v>=1?`$${v.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})}`:`$${v.toFixed(6)}`;
function filterMarkets(f){marketFilter=f; document.querySelectorAll('.chart-filters .chart-filter').forEach(b=>b.classList.remove('active')); document.querySelector(`.chart-filter[data-filter="${f}"]`)?.classList.add('active'); renderMarkets();}
function renderMarkets(){const tbody=document.getElementById('markets-body'); if(!tbody)return; let f=[...cryptoCoins]; if(marketFilter==='gainers')f=f.filter(c=>c.ch>0).sort((a,b)=>b.ch-a.ch); if(marketFilter==='losers')f=f.filter(c=>c.ch<0).sort((a,b)=>a.ch-b.ch); tbody.innerHTML=f.map((c,i)=>`<tr><td>${i+1}</td><td><strong>${c.s}</strong></td><td>${fmtUSD(c.p)}</td><td class="crypto-change ${c.ch>=0?'positive':'negative'}">${c.ch}%</td><td><button class="btn-chart-export" onclick="addToWatchlist('${c.s}')"><i class="fas fa-star"></i></button></td></tr>`).join('');}
function renderWatchlist(){const c=document.getElementById('watchlist-container'); if(!c)return; const l=cryptoCoins.filter(c=>(localStorage.getItem('moneo_w')||'["BTC","ETH","SOL"]').split(',').map(s=>s.replace(/"/g,'')).includes(c.s)); c.innerHTML=l.map(c=>`<div class="watchlist-card"><button class="watchlist-remove" onclick="removeFromWatchlist('${c.s}')"><i class="fas fa-times"></i></button><div style="display:flex;justify-content:space-between;"><div><strong>${c.s}</strong><small style="display:block;color:var(--text-muted)">${c.n}</small></div><div class="crypto-change ${c.ch>=0?'positive':'negative'}">${c.ch}%</div></div><div style="font-family:monospace;font-size:1.1rem;">${fmtUSD(c.p)}</div></div>`).join('');}
function addToWatchlist(s){let w=JSON.parse(localStorage.getItem('moneo_w')||'["BTC","ETH","SOL"]'); if(!w.includes(s)){w.push(s); localStorage.setItem('moneo_w',JSON.stringify(w)); renderWatchlist(); showNotification('Watchlist',`${s} ajouté.`,'success');}}
function removeFromWatchlist(s){let w=JSON.parse(localStorage.getItem('moneo_w')||'["BTC","ETH","SOL"]'); w=w.filter(x=>x!==s); localStorage.setItem('moneo_w',JSON.stringify(w)); renderWatchlist(); showNotification('Watchlist',`${s} retiré.`,'info');}
function openWatchlistManager(){renderWatchlist();}
function renderPortfolio(){const ctx=document.getElementById('portfolioChart'); if(!ctx)return; if(portfolioChart)portfolioChart.destroy(); portfolioChart=new Chart(ctx,{type:'doughnut',data:{labels:Object.keys(cryptoPortfolio),datasets:[{data:Object.values(cryptoPortfolio).map((v,i)=>v*cryptoCoins.find(c=>c.s===Object.keys(cryptoPortfolio)[i])?.p||0),borderWidth:0}]},options:{responsive:true,maintainAspectRatio:false,cutout:'65%',plugins:{legend:{display:false}}}}); document.getElementById('crypto-total-value').innerText=fmtUSD(Object.keys(cryptoPortfolio).reduce((s,k)=>s+cryptoPortfolio[k]*(cryptoCoins.find(c=>c.s===k)?.p||0),0));}
function openCryptoAction(type,pre=''){document.getElementById('crypto-action-title').innerText={buy:'💰 Acheter',sell:'💸 Vendre',stake:'🔒 Staker',convert:'🔄 Convertir'}[type]; if(pre)document.getElementById('crypto-asset-select').value=pre; openModal('crypto-action-modal');}
document.getElementById('crypto-action-confirm').onclick=()=>{const s=document.getElementById('crypto-asset-select').value, a=parseFloat(document.getElementById('crypto-action-amount').value); if(!s||!a)return; cryptoPortfolio[s]=(cryptoPortfolio[s]||0)+a; cryptoHistory.unshift({date:new Date().toISOString(),type:'buy',symbol:s,amount:a,total:a*100}); localStorage.setItem('moneo_p',JSON.stringify(cryptoPortfolio)); localStorage.setItem('moneo_h',JSON.stringify(cryptoHistory)); closeModal('crypto-action-modal'); renderPortfolio(); showNotification('✅','Transaction enregistrée.','success');};
function exportCryptoHistoryToCSV(){if(cryptoHistory.length===0)return; let csv='Date,Type,Actif,Qté,Total\n'; cryptoHistory.forEach(h=>{csv+=`${h.date},${h.type},${h.symbol},${h.amount},${h.total}\n`}); const b=new Blob([csv],{type:'text/csv'}), l=document.createElement('a'); l.href=URL.createObjectURL(b); l.download='BitWise_Crypto_History.csv'; l.click(); showNotification('📥','CSV téléchargé.','success');}
function renderOrderBook(){const c=document.getElementById('order-book'), p=cryptoCoins.find(x=>x.s==='BTC')?.p||60000; if(!c)return; let h=''; for(let i=1;i<=5;i++){const s=p*(1+(Math.random()-0.5)*0.001*i); h+=`<div class="ob-row ob-ask"><span>${s.toFixed(2)}</span><div class="ob-bar" style="width:${Math.random()*30}%;background:var(--danger);"></div></div>`;} h+=`<div class="ob-spread">${p} $</div>`; for(let i=5;i>=1;i--){const s=p*(1-(Math.random()-0.5)*0.001*i); h+=`<div class="ob-row ob-bid"><span>${s.toFixed(2)}</span><div class="ob-bar" style="width:${Math.random()*30}%;background:var(--accent);"></div></div>`;} c.innerHTML=h;}
function placeAdvancedOrder(t){const p=parseFloat(document.getElementById('order-price').value), q=parseFloat(document.getElementById('order-qty').value); if(!p||!q)return; showNotification(`📤 Ordre ${t.toUpperCase()} placé`,'warning');}
function renderPnl(){const ctx=document.getElementById('pnlChart'); if(!ctx)return; const inv=5000, cur=currentUser.solde, p=((cur-inv)/inv)*100; document.getElementById('pnl-invested').innerText=inv.toFixed(0)+' $'; document.getElementById('pnl-diff').innerText=`${p>=0?'+':''}${p.toFixed(2)}%`; document.getElementById('pnl-diff').className=p>=0?'pnl-positive':'pnl-negative'; const d=pnlHistory[1]||[]; d.push(p); if(d.length>20)d.shift(); pnlHistory[1]=d; localStorage.setItem('moneo_pnl',JSON.stringify(pnlHistory)); if(pnlChart)pnlChart.destroy(); pnlChart=new Chart(ctx,{type:'line',data:{labels:d.map((_,i)=>i),datasets:[{data:d,borderColor:p>=0?'#10b981':'#ef4444',tension:0.4,pointRadius:0,fill:true}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{display:false},y:{display:false}}}});}
function updatePnl(){renderPnl();}
function openDCAModal(){openModal('dca-modal');} function saveDCA(){closeModal('dca-modal'); showNotification('✅','DCA activé.','success');}
function openFeeCalculator(){openModal('fee-calc-modal');} function calculateNetworkFee(){document.getElementById('fee-results').style.display='block'; document.getElementById('fee-results').innerHTML='<div class="fee-result-row"><span>Frais :</span><strong>2.45 $</strong></div>';}
function open2faSetup(){document.getElementById('twofa-secret-display').innerText=Math.floor(100000+Math.random()*900000); openModal('twofa-setup-modal');} function verify2faSetup(){securityState.enabled=true; localStorage.setItem('moneo_2fa','true'); closeModal('twofa-setup-modal'); showNotification('🔒','2FA Activé.','success');}
function verifyLockCode(){if(document.getElementById('lock-code-input').value.length>=4||document.getElementById('lock-code-input').value==='123456'){securityState.locked=false; document.getElementById('session-lock-overlay').style.display='none'; showNotification('✅','Déverrouillé.');}else showNotification('❌','Code invalide.','error');}
function forceLogout(){localStorage.removeItem('moneo_last_user'); location.reload();}
function initFloatingWidget(){updateWidgetPrices(); setInterval(updateWidgetPrices,4000);} function updateWidgetPrices(){const b=cryptoCoins.find(c=>c.s==='BTC'), e=cryptoCoins.find(c=>c.s==='ETH'), s=cryptoCoins.find(c=>c.s==='SOL'); if(b){document.getElementById('float-btc-price').innerText=fmtUSD(b.p); document.getElementById('float-btc-change').innerText=`${b.ch>=0?'+':''}${b.ch}%`; document.getElementById('float-btc-change').style.color=b.ch>=0?'var(--accent)':'var(--danger)';} if(e)document.getElementById('float-eth-price').innerText=fmtUSD(e.p); if(s)document.getElementById('float-sol-price').innerText=fmtUSD(s.p);} function toggleWidgetExpand(){document.getElementById('crypto-float-widget').classList.toggle('expanded');}
setInterval(()=>{if(securityState.enabled&&Date.now()-securityState.lastActivity>300000&&!securityState.locked){securityState.locked=true; document.getElementById('session-lock-overlay').style.display='flex';}},10000);
window.addEventListener('mousemove',()=>securityState.lastActivity=Date.now());
document.getElementById('lang-selector').onchange=e=>{ const v=e.target.value; localStorage.setItem('moneo_lang',v); applyLanguage(v); };
// === Auto-translation engine =================================================
const I18N = { current: 'FR', originals: [], dicts: {}, busy: false, observerStarted: false }; window.I18N = I18N;
const I18N_RTL = new Set(['AR','HE','FA','UR','PS']);
function i18nUpdateDocAttrs(lang){ const code = (lang||'FR').toLowerCase().replace('-','-'); try{ document.documentElement.setAttribute('lang', code); document.documentElement.setAttribute('dir', I18N_RTL.has((lang||'').toUpperCase()) ? 'rtl' : 'ltr'); }catch{} }
const I18N_SKIP_TAGS = new Set(['SCRIPT','STYLE','NOSCRIPT','CODE','PRE']); const I18N_ATTRS = ['placeholder','title','alt','aria-label']; const I18N_NUM_RE = /^[\s0-9.,:;\-+*/€$%()\[\]<>=]+$/;
function i18nIsTranslatable(s){ if(!s) return false; const t=s.trim(); if(t.length<2) return false; if(I18N_NUM_RE.test(t)) return false; return /[A-Za-zÀ-ÿ]/.test(t); }
function i18nNodeAllowed(el){ if(!el) return false; if(I18N_SKIP_TAGS.has(el.tagName)) return false; if(el.id==='lang-selector' || (el.closest && el.closest('#lang-selector'))) return false; if(el.dataset && el.dataset.i18nSkip!==undefined) return false; return true; }
function i18nCaptureFrom(root){ const added=[]; const walker=document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode(n){ const p=n.parentElement; if(!p || !i18nNodeAllowed(p)) return NodeFilter.FILTER_REJECT; if(!i18nIsTranslatable(n.nodeValue)) return NodeFilter.FILTER_REJECT; return NodeFilter.FILTER_ACCEPT; } }); let n; while((n=walker.nextNode())){ if(n.__i18nIdx!==undefined) continue; const rec={kind:'text', node:n, original:n.nodeValue}; n.__i18nIdx=I18N.originals.length; I18N.originals.push(rec); added.push(rec); } const elements = root.nodeType===1 ? [root, ...root.querySelectorAll('*')] : root.querySelectorAll('*'); elements.forEach(el=>{ if(!i18nNodeAllowed(el)) return; I18N_ATTRS.forEach(a=>{ const v=el.getAttribute && el.getAttribute(a); if(v && i18nIsTranslatable(v) && !el.__i18nAttr?.[a]){ const rec={kind:'attr', node:el, attr:a, original:v}; el.__i18nAttr=el.__i18nAttr||{}; el.__i18nAttr[a]=I18N.originals.length; I18N.originals.push(rec); added.push(rec); } }); }); return added; }
function i18nApplyDict(records, dict){ records.forEach(r=>{ const key=r.original.trim(); const tr=dict.get(key); if(!tr) return; const lead=r.original.match(/^\s*/)[0]; const trail=r.original.match(/\s*$/)[0]; const finalText=lead+tr+trail; if(r.kind==='text'){ r.node.nodeValue=finalText; } else { r.node.setAttribute(r.attr, finalText); } }); }
function i18nRestoreOriginals(){ I18N.originals.forEach(r=>{ if(r.kind==='text'){ r.node.nodeValue=r.original; } else { r.node.setAttribute(r.attr, r.original); } }); }
async function i18nFetchTranslations(lang, texts){ try{ const res=await fetch('/api/translate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({texts,targetLang:lang})}); if(!res.ok) throw new Error('http '+res.status); const data=await res.json(); return Array.isArray(data.translations)?data.translations:null; }catch(err){ return null; } }
function i18nLoadCache(lang){ try{ const raw=localStorage.getItem('moneo_i18n_'+lang); if(!raw) return new Map(); return new Map(JSON.parse(raw)); }catch{ return new Map(); } }
function i18nSaveCache(lang, dict){ try{ localStorage.setItem('moneo_i18n_'+lang, JSON.stringify([...dict.entries()].slice(-2000))); }catch{} }
async function applyLanguage(lang){ lang=(lang||'FR').toUpperCase(); I18N.current=lang; i18nUpdateDocAttrs(lang); if(I18N.originals.length===0) i18nCaptureFrom(document.body); if(lang==='FR'){ i18nRestoreOriginals(); i18nStartObserver(); return; } const dict=I18N.dicts[lang]||i18nLoadCache(lang); I18N.dicts[lang]=dict; const missing=[]; const seen=new Set(); I18N.originals.forEach(r=>{ const k=r.original.trim(); if(!dict.has(k) && !seen.has(k)){ seen.add(k); missing.push(k); } }); if(missing.length>0){ I18N.busy=true; try{ if(typeof showNotification==='function') showNotification('🌍','Traduction en cours…','info'); }catch{} for(let i=0;i<missing.length;i+=80){ const chunk=missing.slice(i,i+80); const out=await i18nFetchTranslations(lang, chunk); if(out){ chunk.forEach((src,idx)=>{ if(out[idx]) dict.set(src, out[idx]); }); } } i18nSaveCache(lang, dict); I18N.busy=false; } i18nApplyDict(I18N.originals, dict); i18nStartObserver(); try{ if(typeof showNotification==='function') showNotification('🌍','Langue : '+lang,'success'); }catch{} }
function i18nStartObserver(){ if(I18N.observerStarted) return; I18N.observerStarted=true; const mo=new MutationObserver(muts=>{ const fresh=[]; muts.forEach(m=>{ m.addedNodes.forEach(node=>{ if(node.nodeType===1){ fresh.push(...i18nCaptureFrom(node)); } else if(node.nodeType===3 && node.parentElement && i18nNodeAllowed(node.parentElement) && i18nIsTranslatable(node.nodeValue) && node.__i18nIdx===undefined){ const rec={kind:'text', node, original:node.nodeValue}; node.__i18nIdx=I18N.originals.length; I18N.originals.push(rec); fresh.push(rec); } }); }); if(fresh.length===0 || I18N.current==='FR') return; const dict=I18N.dicts[I18N.current]; if(!dict) return; const missing=[]; fresh.forEach(r=>{ const k=r.original.trim(); if(!dict.has(k)) missing.push(k); }); i18nApplyDict(fresh, dict); if(missing.length>0 && !I18N.busy){ I18N.busy=true; i18nFetchTranslations(I18N.current, [...new Set(missing)]).then(out=>{ if(out){ [...new Set(missing)].forEach((src,idx)=>{ if(out[idx]) dict.set(src,out[idx]); }); i18nSaveCache(I18N.current,dict); i18nApplyDict(fresh,dict); } I18N.busy=false; }); } }); mo.observe(document.body,{childList:true, subtree:true, characterData:false}); }
(function(){ const saved=localStorage.getItem('moneo_lang'); if(saved){ const sel=document.getElementById('lang-selector'); if(sel){ sel.value=saved; } } setTimeout(()=>{ i18nCaptureFrom(document.body); if(saved && saved!=='FR') applyLanguage(saved); else i18nStartObserver(); }, 50); })();
// ============================================================================
setTimeout(()=>{if(securityState.enabled&&!securityState.locked){securityState.locked=true; document.getElementById('session-lock-overlay').style.display='flex';}},2000);
</script>
<div id="export-template" style="position: absolute; top: 0; left: 0; z-index: -1000; opacity: 0; pointer-events: none; width: 800px; padding: 40px; background: #fff; color: #000; font-family: sans-serif; box-sizing: border-box;">
<div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:40px; border-bottom:2px solid #000; padding-bottom:20px;">
<div><h1 id="export-title" style="margin:0; font-size:24px; color:#1a1a1a;">Titre</h1><p id="export-date" style="margin:10px 0 0 0; color:#666;">Date: ...</p></div>
<div style="text-align:right;"><div style="font-size: 28px; font-weight: 700; color: #1a1a1a; display: flex; align-items: center; justify-content: flex-end; gap: 8px;"><i class="fas fa-layer-group" style="color: #3b82f6;"></i><span style="color: #3b82f6;">Bit Wise</span></div><p style="margin:5px 0 0 0; font-size:12px; color:#666;">La banque nouvelle génération</p></div>
</div>
<div style="margin-bottom:30px; background:#f8fafc; padding:15px; border-radius:8px;"><h3 style="margin-top:0; color:#333;">Informations du titulaire</h3><p style="margin:5px 0; color:#000;"><strong>Nom complet :</strong> <span id="export-fullname">...</span></p><p style="margin:5px 0; color:#000;"><strong>IBAN :</strong> <span id="export-iban">...</span></p><p style="margin:5px 0; color:#000;"><strong>BIC :</strong> <span id="export-bic">...</span></p></div>
<div id="export-content" style="min-height:300px; color:#000;"></div>
<div style="margin-top:40px; border-top:1px solid #ccc; padding-top:15px; text-align:center; font-size:10px; color:#666;">2026 Bit Wise – Société Anonyme • RCS Paris 803 542 709 • Agrément ACPR 49375 • Adhérent FGDR</div>
</div>
<script>
async function exportDocument(type, format) {
if (!currentUser) return;
document.getElementById('export-fullname').innerText = ((currentUser.prenom || '') + ' ' + (currentUser.nom || '')).trim() || 'Non renseigné';
document.getElementById('export-iban').innerText = currentUser.iban || 'Non renseigné'; document.getElementById('export-bic').innerText = currentUser.bic || 'MONEFRPPXXX';
const dateStr = new Date().toLocaleDateString('fr-FR', {year: 'numeric', month: 'long', day: 'numeric'}); document.getElementById('export-date').innerText = 'Date : ' + dateStr;
let title = '', contentHtml = '';
if (type === 'releve') {
title = 'Relevé Bancaire';
let rows = (currentUser.transactions || []).slice().reverse().map(t => { return `<tr><td style="padding:8px; border-bottom:1px solid #eee;">${t.date || new Date().toLocaleDateString()}</td><td style="padding:8px; border-bottom:1px solid #eee;">${t.desc}</td><td style="padding:8px; border-bottom:1px solid #eee; text-align:right; color:${t.amount >= 0 ? '#15803d' : '#dc2626'}">${t.amount >= 0 ? '+' : ''}${t.amount.toFixed(2)} €</td></tr>`; }).join('');
if (!rows) rows = '<tr><td colspan="3" style="padding:8px; text-align:center;">Aucune transaction</td></tr>';
contentHtml = `<h4 style="color:#333; margin-top:0;">Dernières opérations</h4><table style="width:100%; border-collapse:collapse; font-size:14px;"><thead><tr style="background:#f1f5f9; text-align:left;"><th style="padding:8px; border-bottom:2px solid #cbd5e1;">Date</th><th style="padding:8px; border-bottom:2px solid #cbd5e1;">Description</th><th style="padding:8px; border-bottom:2px solid #cbd5e1; text-align:right;">Montant</th></tr></thead><tbody>${rows}</tbody></table><div style="text-align:right; margin-top:20px; font-size:16px;"><strong>Solde actuel : ${(currentUser.solde || 0).toFixed(2)} €</strong></div>`;
} else if (type === 'rib') { title = 'Relevé d\'Identité Bancaire (RIB)'; contentHtml = `<div style="text-align:center; padding:40px 20px; border:2px dashed #cbd5e1; border-radius:8px; margin-top:20px;"><p style="font-size:18px; margin-bottom:10px;">Ce document vous permet de communiquer vos coordonnées bancaires.</p></div>`; } else if (type === 'historique_demandes') {
title = 'Historique des demandes'; let historyHtml = '';
if (currentUser.creditHistory && currentUser.creditHistory.length > 0) { historyHtml = currentUser.creditHistory.slice().reverse().map(h => { let statusColor = h.status==='approved'?'#15803d':(h.status==='rejected'?'#dc2626':'#ca8a04'); let statusText = h.status==='approved'?'Approuvé':(h.status==='rejected'?'Refusé':'En cours'); return `<div style="padding:15px; border:1px solid #e2e8f0; border-radius:8px; margin-bottom:15px;"><div style="display:flex; justify-content:space-between; margin-bottom:8px;"><strong style="font-size:16px;">${h.amount} € sur ${h.duration} mois</strong><span style="color:${statusColor}; font-weight:bold; background:#f8fafc; padding:2px 8px; border-radius:12px;">${statusText}</span></div><div style="font-size:14px; color:#64748b;">Projet : ${h.projectType}<br>Mensualité : ${h.monthlyPayment} €<br>Date : ${h.date || dateStr}</div></div>`; }).join(''); } else { historyHtml = '<p style="text-align:center; color:#666; padding:20px;">Aucune demande de crédit.</p>'; }
contentHtml = `<h4 style="color:#333; margin-top:0;">Vos demandes de crédit</h4>${historyHtml}`;
}
document.getElementById('export-title').innerText = title; document.getElementById('export-content').innerHTML = contentHtml;
const element = document.getElementById('export-template'); const filename = `BitWise_${type}_${new Date().getTime()}`;
try {
if (format === 'pdf') { const opt = { margin: 10, filename: filename + '.pdf', image: { type: 'jpeg', quality: 0.98 }, html2canvas: { scale: 2, useCORS: true, windowWidth: 800 }, jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' } }; await html2pdf().set(opt).from(element).save(); }
else if (format === 'jpg') { const canvas = await html2canvas(element, { scale: 2, useCORS: true, windowWidth: 800 }); const link = document.createElement('a'); link.download = filename + '.jpg'; link.href = canvas.toDataURL('image/jpeg', 0.98); link.click(); }
} catch(err) { if (typeof showNotification === 'function') showNotification('❌', 'Erreur lors de l\'exportation.', 'danger'); }
}
</script>
</body>
</html>
