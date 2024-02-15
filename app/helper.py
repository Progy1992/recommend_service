def get_recommendations(user_id, model, n=10):
    # Convert the user's ratings to an anti-testset (books the user hasn't rated)
    testset = [[user_id, isbn, 0] for isbn in ratings['isbn'].unique() if isbn not in ratings[ratings['user_id'] == user_id]['isbn']]
    predictions = model.test(testset)

    # Get the top N recommendations
    top_n_predictions = sorted(predictions, key=lambda x: x.est, reverse=True)[:n]

    recommended_books = [(pred.iid, pred.est) for pred in top_n_predictions]
    return recommended_books