def get_result(prediction):
    """create dictionary and assign predicted class"""
    
    classes = ["NOT_drinking_coffee", "drinking_coffee"]
    
    if prediction[0] > prediction[1]:
        return {"probability": prediction[0], "class": classes[0]}
    else:
        return {"probability": prediction[1], "class": classes[1]}