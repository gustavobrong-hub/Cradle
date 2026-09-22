"""Calculadora de economia unitária (low ticket Hotmart + Meta Ads).

Premissas do usuário:
- Produto principal: taxa fixa ~US$ 1,49 por venda; líquido ~74% num ticket de US$ 9,90.
  => taxa variável implícita v = 1 - (0,74*9,90 + 1,49)/9,90 ≈ 10,95%.
- Bumps: líquido ~88%.
Definição de ROI usada (explícita): ROI = faturamento líquido (após taxas Hotmart e reembolsos) ÷ gasto em anúncios.
  (É a leitura compatível com a régua "sobe verba com ROI > 1,5" e com o baseline do Mimo Gift.)
  CPA de break-even = líquido por comprador (ROI = 1,0).
  CPA máximo pra régua = líquido por comprador ÷ 1,5.
  Se a conta de anúncio for em BRL, o UTMify aplica 12% de imposto sobre o gasto por padrão
  → CPA de anúncio máximo = líquido ÷ (1,5 × 1,12).
Uso: python3 calc_economia.py
"""
FIXED = 1.49
VAR = 1 - (0.74 * 9.90 + FIXED) / 9.90
BUMP_NET = 0.88
FX = {"USD": 1.0, "BRL": 5.14, "MXN": 17.22, "COP": 3116.0, "CLP": 959.5, "PEN": 3.366}


def front_net(price):
    return price * (1 - VAR) - FIXED


def economics(front, bumps, refund=0.03, roi_target=1.5, meta_tax=0.0):
    """bumps: lista de (nome, preço, adesão 0-1). Retorna dict com AOV e CPAs em US$."""
    gross = front + sum(p * t for _, p, t in bumps)
    net = front_net(front) + sum(p * t * BUMP_NET for _, p, t in bumps)
    net_after_refund = net * (1 - refund)
    be = net_after_refund
    cpa_target = net_after_refund / (roi_target * (1 + meta_tax))
    return {
        "front": front,
        "aov_bruto": round(gross, 2),
        "liquido_front": round(front_net(front), 2),
        "liquido_por_comprador": round(net_after_refund, 2),
        "cpa_break_even": round(be, 2),
        f"cpa_roi_{roi_target}": round(cpa_target, 2),
        "pct_liquido_sobre_bruto": round(100 * net_after_refund / gross, 1),
    }


if __name__ == "__main__":
    print(f"taxa variável implícita no front: {VAR*100:.2f}% + US$ {FIXED}")
    # Referência ilustrativa: front 9,90 + 1 bump barato com ~1/3 de adesão
    ref = economics(9.90, [("bump", 4.90, 0.33)], refund=0.01)
    print("Referência ilustrativa:", ref)
    for front in (5.90, 6.90, 7.90, 8.90, 9.90, 11.90, 14.90):
        e = economics(front, [("bump1", 4.90, 0.30), ("bump2", 4.90, 0.15), ("bump3", 6.90, 0.08)], refund=0.04)
        print(front, e)
