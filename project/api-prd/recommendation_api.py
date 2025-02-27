# Salve este arquivo como recommendation_api.py
import pickle
import numpy as np
import scipy.sparse as sparse
from fastapi import FastAPI, HTTPException

# Inicializa a aplicação FastAPI
app = FastAPI(title="API de Recomendação", description="API para modelo de recomendação ALS")

# Carrega o modelo
try:
    with open('als_model_v2.pkl', 'rb') as f:
        model_data = pickle.load(f)
        
    model = model_data['model']
    user_id_map = model_data['user_id_map']
    item_id_map = model_data['item_id_map']
    reverse_user_map = model_data['reverse_user_map']
    reverse_item_map = model_data['reverse_item_map']
    items_pop = model_data["items_popularity"]
    
    print("Modelo carregado com sucesso")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    model = None
    user_id_map = {}
    item_id_map = {}
    reverse_user_map = {}
    reverse_item_map = {}
    
# Rota para recomendar itens a um usuário existente
@app.get("/recommend/{user_id}")
def recommend_for_user(user_id: str, num_recommendations: int = 10):
    """
    Retorna recomendações para um usuário com base no modelo treinado
    """
    if model is None:
        raise HTTPException(status_code=500, detail="Modelo não carregado")
    
    if user_id not in user_id_map:
        try:
            recommendations = [
                {
                    "item_id": idx, 
                    "score": 0
                }
                for idx in items_pop[0:10]
            ]
            return {"recommendations": recommendations}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao gerar recomendações: {str(e)}")
    
    try:
        user_idx = user_id_map[user_id]
        # Cria um vetor esparso para o usuário com valores zerados
        user_items = sparse.csr_matrix((1, len(item_id_map)))
        
        # Gera recomendações
        recommended_items, scores = model.recommend(
            userid=user_idx,
            user_items=user_items,
            N=num_recommendations,
            filter_already_liked_items=True
        )
        
        # Formata as recomendações
        recommendations = [
            {
                "item_id": reverse_item_map[item_idx],
                "score": float(score)
            }
            for item_idx, score in zip(recommended_items, scores)
        ]
        
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar recomendações: {str(e)}")

# Rota para verificar o status da API
@app.get("/health")
def health_check():
    """Verifica se o serviço está funcionando corretamente"""
    if model is None:
        return {"status": "erro", "message": "Modelo não carregado"}
    return {"status": "ativo", "model_loaded": True}

# Rota para obter informações sobre o modelo
@app.get("/model-info")
def model_info():
    """Retorna informações sobre o modelo carregado"""
    if model is None:
        raise HTTPException(status_code=500, detail="Modelo não carregado")
    
    return {
        "tipo_de_modelo": "Alternating Least Squares (ALS)",
        "num_usuarios": len(user_id_map),
        "num_itens": len(item_id_map),
        "fatores": model.factors,
        "regularizacao": model.regularization,
        "iteracoes": model.iterations
    }

# Para rodar a API: uvicorn recommendation_api:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)