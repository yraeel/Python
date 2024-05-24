def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""
    profile = {}

    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile 
        
user_profile = build_profile('Israel', 'Machado', location = 'rio de janeiro', field = 'developer')
    
print(user_profile)