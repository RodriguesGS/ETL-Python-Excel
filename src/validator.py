from pydantic import BaseModel, Field
from typing import Optional

class PlanilhaVendas(BaseModel):
    Organizador: int = Field(..., description="ID do Organizador")
    Ano_Mes: str = Field(..., description="Ano e mes do registro")
    Dia_da_Semana: str = Field(..., description="Dia da semana correspondente a data")
    Tipo_Dia: str = Field(..., description="Tipo do dia (util, fim de semana, feriado)")
    Objetivo: str = Field(..., description="Objetivo da campanha ou ação")
    Date: str = Field(..., description="Data do registro no formato YYYY-MM-DD")
    AdSet_name: Optional[str] = Field(None, description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(0.0, ge=0, le=1200.00, description="Valor gasto na campanha")
    Link_clicks: Optional[float] = Field(None, description="Número de cliques no link", nullable=True)
    Impressions: int = Field(0, description="Número de impressões", nullable=True)
    Conversions: Optional[float] = Field(None, description="Número de conversões", nullable=True)
    Segmentacao: Optional[float] = Field(None, description="Segmentação utilizada na campanha")
    Tipo_de_Anúncio: str = Field(..., description="Tipo de anúncio utilizado")
    Fase: str = Field(..., description="Fase da campanha")