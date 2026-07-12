print("=======================================")
print("         SMART CROP ADVISOR            ")
print("=======================================")

while True:
      print("\n1. Crop Recommendation")
      print("2. Crop Information")
      print("3. Farming Cost Estimator")
      print("4. Farming Tips")
      print("5. Exit\n")

      choice=int(input("enter your choice: "))

      match choice:
            case 1:
                 print("\n---Crop Recommendation---")

                 print("\nSeason:-\n")
                 print("1. Kharif")
                 print("2. Rabi")
                 print("3. Zaid\n")
                 season=int(input("Enter Season: "))
                 print("\nSoil Type:-\n")
                 print("1. Black Soil")
                 print("2. Red Soil")
                 print("3. Sandy Soil")
                 print("4. Loamy Soil\n")
                 soil=int(input("Enter Soil: "))
                 print("\nWater Availability:-\n")
                 print("1. Low")
                 print("2. Medium")
                 print("3. High\n")
                 water=int(input("enter Water Level: "))         
           
                 match season:
                       case 1:
                            match soil:
                                  case 1:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Pearl Millet(Bajra)")
                                                  print("Reason: Bajra is drought-tolerant.")   
                                             case 2:
                                                  print("\nRecommended Crop: Soyabean")
                                                  print("Reason: Soybean performs well with moderate water.")
                                             case 3:
                                                  print("\nRecommended Crop: Cotton")
                                                  print("Reason: Cotton grows well in black soil with good rainfall.")
                                             case __:
                                                  print("No Crop")
                                  case 2:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Mustard")
                                                  print("Reason: Drought-tolerant crop.")   
                                             case 2:
                                                  print("\nRecommended Crop: Gram")
                                                  print("Reason: Good choice for red soil.")
                                             case 3:
                                                  print("\nRecommended Crop: Wheat")
                                                  print("Reason: Productive with sufficient irrigation.")
                                             case __:
                                                  print("No Crop")
                                  case 3:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Barley")
                                                  print("Reason: Requires less water than wheat.")   
                                             case 2:
                                                  print("\nRecommended Crop: Mustard")
                                                  print("Reason: Performs well in sandy soils.")
                                             case 3:
                                                  print("\nRecommended Crop: Potato")
                                                  print("Reason: Sandy soil supports tuber growth with irrigation.")
                                             case __:
                                                  print("No Crop")
                                  case 4:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Pigeon Pea (Tur)")
                                                  print("Reason: Can tolerate relatively dry.")   
                                             case 2:
                                                  print("\nRecommended Crop: Maize")
                                                  print("Reason: One of the best choices for loamy soil.")
                                             case 3:
                                                  print("\nRecommended Crop: Rice")
                                                  print("Reason: Loamy soil retains water well.")
                                             case __:
                                                  print("No Crop")

                       case 2:
                            match soil:
                                  case 1:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Mustard")
                                                  print("Reason: Can grow with limited water.")   
                                             case 2:
                                                  print("\nRecommended Crop: Gram (Chickpea)")
                                                  print("Reason: Requires moderate water.")
                                             case 3:
                                                  print("\nRecommended Crop: Wheat")
                                                  print("Reason: Wheat grows well with irrigation.")
                                             case __:
                                                  print("No Crop")
                                  case 2:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Mustard")
                                                  print("Reason: Drought-tolerant crop.")   
                                             case 2:
                                                  print("\nRecommended Crop: Gram")
                                                  print("Reason: Good choice for red soil.")
                                             case 3:
                                                  print("\nRecommended Crop: Wheat")
                                                  print("Reason: Productive with sufficient irrigation.")
                                             case __:
                                                  print("No Crop")
                                  case 3:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Barley")
                                                  print("Reason: Requires less water than wheat.")   
                                             case 2:
                                                  print("\nRecommended Crop: Mustard")
                                                  print("Reason: Performs well in sandy soils.")
                                             case 3:
                                                  print("\nRecommended Crop: Potato")
                                                  print("Reason: Sandy soil supports tuber growth with irrigation.")
                                             case __:
                                                  print("No Crop")
                                  case 4:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Mustard")
                                                  print("Reason: Suitable for lower moisture conditions.")   
                                             case 2:
                                                  print("\nRecommended Crop: Pea")
                                                  print("Reason: Thrives in fertile loamy soil.")
                                             case 3:
                                                  print("\nRecommended Crop: Wheat")
                                                  print("Reason: One of the best combinations.")
                                             case __:
                                                  print("No Crop")

                       case 3:
                            match soil:
                                  case 1:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Sesame (Til)")
                                                  print("Reason: Can tolerate dry conditions.")   
                                             case 2:
                                                  print("\nRecommended Crop: Cucumber")
                                                  print("Reason: Needs moderate water.")
                                             case 3:
                                                  print("\nRecommended Crop: Watermelon")
                                                  print("Reason: Summer crop with irrigation.")
                                             case __:
                                                  print("No Crop")
                                  case 2:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Sesame (Til)")
                                                  print("Reason: Heat- and drought-tolerant.")   
                                             case 2:
                                                  print("\nRecommended Crop: Cucumber")
                                                  print("Reason: Grows well in summer.")
                                             case 3:
                                                  print("\nRecommended Crop: Muskmelon")
                                                  print("Reason: Suitable for warm weather and irrigation.")
                                             case __:
                                                  print("No Crop")
                                  case 3:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Sesame (Til)")
                                                  print("Reason: Needs less water.")   
                                             case 2:
                                                  print("\nRecommended Crop: Muskmelon")
                                                  print("Reason: Prefers sandy, well-drained soil.")
                                             case 3:
                                                  print("\nRecommended Crop: Watermelon")
                                                  print("Reason: Excellent for sandy soil.")
                                             case __:
                                                  print("No Crop")
                                  case 4:
                                       match water:
                                             case 1:
                                                  print("\nRecommended Crop: Sesame (Til)")
                                                  print("Reason: Suitable for dry summer conditions.")   
                                             case 2:
                                                  print("\nRecommended Crop: Watermelon")
                                                  print("Reason: Performs well in fertile loamy soil.")
                                             case 3:
                                                  print("\nRecommended Crop: Cucumber")
                                                  print("Reason: Productive with irrigation.")
                                             case __:
                                                  print("No Crop")

            case 2:
                 print("\n---Crop Information---\n")
                 print("1. Wheat")
                 print("2. Rice")
                 print("3. Cotton")
                 print("4. Soyabean")
                 print("5. Maize")
                 print("6. Mustard")
                 print("7. Groundnut")
                 print("8. Bajra")
                 print("9. Watermelon")
                 print("10. Cucumber\n")
                 crop=int(input("Enter your choice: "))
           
                 match crop:
                       case 1:
                            print("\n----- WHEAT -----")
                            print("Season        : Rabi")
                            print("Soil          : Loamy")
                            print("Water Need    : Medium")
                            print("Harvest Time  : 120 Days")
                            print("Expected Yield: 18-22 Quintals/Acre")
                       case 2:
                            print("\n----- RICE -----")
                            print("Season        : Kharif")
                            print("Soil          : Loamy")
                            print("Water Need    : High")
                            print("Harvest Time  : 120-150 Days")
                            print("Expected Yield: 20-25 Quintals/Acre")
                       case 3:
                            print("\n----- COTTON -----")
                            print("Season        : Kharif")
                            print("Soil          : Black")
                            print("Water Need    : High")
                            print("Harvest Time  : 180 Days")
                            print("Expected Yield: 8-10 Quintals/Acre")
                       case 4:
                            print("\n----- SOYABEAN -----")
                            print("Season        : Kharif")
                            print("Soil          : Black")
                            print("Water Need    : Medium")
                            print("Harvest Time  : 100 Days")
                            print("Expected Yield: 10-15 Quintals/Acre")
                       case 5:
                            print("\n----- MAIZE -----")
                            print("Season        : Kharif")
                            print("Soil          : Loamy")
                            print("Water Need    : Medium")
                            print("Harvest Time  : 100-120 Days")
                            print("Expected Yield: 20-30 Quintals/Acre")
                       case 6:
                            print("\n----- MUSTARD -----")
                            print("Season        : Rabi")
                            print("Soil          : Sandy or Loamy")
                            print("Water Need    : Low")
                            print("Harvest Time  : 110 Days")
                            print("Expected Yield: 18-22 Quintals/Acre")
                       case 7:
                            print("\n----- GROUNDNUT-----")
                            print("Season        : Kharif")
                            print("Soil          : Sandy")
                            print("Water Need    : Medium")
                            print("Harvest Time  : 110 Days")
                            print("Expected Yield: 12-18 Quintals/Acre")
                       case 8:
                            print("\n----- BAJRA -----")
                            print("Season        : Kharif")
                            print("Soil          : Sandy")
                            print("Water Need    : Low")
                            print("Harvest Time  : 80-90 Days")
                            print("Expected Yield: 10-15 Quintals/Acre")
                       case 9:
                            print("\n----- WATERMELON -----")
                            print("Season        : Zaid")
                            print("Soil          : Sandy")
                            print("Water Need    : High")
                            print("Harvest Time  : 90 Days")
                            print("Expected Yield: 100-150 Quintals/Acre")
                       case 10:
                            print("\n----- CUCUMBER -----")
                            print("Season        : Zaid")
                            print("Soil          : Loamy")
                            print("Water Need    : Medium")
                            print("Harvest Time  : 60-70 Days")
                            print("Expected Yield: 80-120 Quintals/Acre")
            case 3:
                 print("\n---Farming Cost Estimator---\n")
                 print("1. Wheat")
                 print("2. Rice")
                 print("3. Cotton")
                 print("4. Soyabean")
                 print("5. Maize")
                 print("6. Mustard")
                 print("7. Groundnut")
                 print("8. Bajra")
                 print("9. Watermelon")
                 print("10. Cucumber\n")
                 crop=int(input("Enter your choice: "))
                 acre=float(input("Enter Land Size (in Acres): "))
           
                 match crop:
                       case 1:
                            seed=2000*acre
                            fertilizer=3000*acre
                            labour=4000*acre
                            irrigation=2000*acre
                            total=seed+fertilizer+labour+irrigation               
                 
                            print("\nCost Report:-\n")
                            print("Crop Name       : Wheat")
                            print("Land Size       :",acre,"Acres\n")
                            print("Seed Cost       :",seed)
                            print("Fertilizer Cost :",fertilizer)
                            print("Labour Cost     :",labour)
                            print("Irrigation Cost :",irrigation)
                            print("\nEstimated Cost  :",total)
                       case 2:
                            seed=2500*acre
                            fertilizer=3500*acre
                            labour=5000*acre
                            irrigation=3000*acre
                            total=seed+fertilizer+labour+irrigation               
                 
                            print("\nCost Report:-\n")
                            print("Crop Name       : Rice")
                            print("Land Size       :",acre,"Acres\n")
                            print("Seed Cost       :",seed)
                            print("Fertilizer Cost :",fertilizer)
                            print("Labour Cost     :",labour)
                            print("Irrigation Cost :",irrigation)
                            print("\nEstimated Cost  :",total)
                       case 3:
                            seed=3500*acre
                            fertilizer=4000*acre
                            labour=6000*acre
                            irrigation=3000*acre
                            total=seed+fertilizer+labour+irrigation               
                 
                            print("\nCost Report:-\n")
                            print("Crop Name       : Cotton")
                            print("Land Size       :",acre,"Acres\n")
                            print("Seed Cost       :",seed)
                            print("Fertilizer Cost :",fertilizer)
                            print("Labour Cost     :",labour)
                            print("Irrigation Cost :",irrigation)
                            print("\nEstimated Cost  :",total)
                       case 4:
                            seed=2000*acre
                            fertilizer=2500*acre
                            labour=3500*acre
                            irrigation=2000*acre
                            total=seed+fertilizer+labour+irrigation               
                 
                            print("\nCost Report:-\n")
                            print("Crop Name       : Soyabean")
                            print("Land Size       :",acre,"Acres\n")
                            print("Seed Cost       :",seed)
                            print("Fertilizer Cost :",fertilizer)
                            print("Labour Cost     :",labour)
                            print("Irrigation Cost :",irrigation)
                            print("\nEstimated Cost  :",total)
                       case 5:
                            seed=2200*acre
                            fertilizer=2800*acre
                            labour=3800*acre
                            irrigation=2000*acre
                            total=seed+fertilizer+labour+irrigation               
                 
                            print("\nCost Report:-\n")
                            print("Crop Name       : Maize")
                            print("Land Size       :",acre,"Acres\n")
                            print("Seed Cost       :",seed)
                            print("Fertilizer Cost :",fertilizer)
                            print("Labour Cost     :",labour)
                            print("Irrigation Cost :",irrigation)
                            print("\nEstimated Cost  :",total)
                       case 6:
                            seed=1800*acre
                            fertilizer=2200*acre
                            labour=3000*acre
                            irrigation=1500*acre
                            total=seed+fertilizer+labour+irrigation               
                 
                            print("\nCost Report:-\n")
                            print("Crop Name       : Mustard")
                            print("Land Size       :",acre,"Acres\n")
                            print("Seed Cost       :",seed)
                            print("Fertilizer Cost :",fertilizer)
                            print("Labour Cost     :",labour)
                            print("Irrigation Cost :",irrigation)
                            print("\nEstimated Cost  :",total)
                       case 7:
                            seed=2500*acre
                            fertilizer=3000*acre
                            labour=4000*acre
                            irrigation=2500*acre
                            total=seed+fertilizer+labour+irrigation               
                 
                            print("\nCost Report:-\n")
                            print("Crop Name       : Groundnut")
                            print("Land Size       :",acre,"Acres\n")
                            print("Seed Cost       :",seed)
                            print("Fertilizer Cost :",fertilizer)
                            print("Labour Cost     :",labour)
                            print("Irrigation Cost :",irrigation)
                            print("\nEstimated Cost  :",total)
                       case 8:
                            seed=1500*acre
                            fertilizer=2000*acre
                            labour=2800*acre
                            irrigation=1500*acre
                            total=seed+fertilizer+labour+irrigation               
                 
                            print("\nCost Report:-\n")
                            print("Crop Name       : Bajra")
                            print("Land Size       :",acre,"Acres\n")
                            print("Seed Cost       :",seed)
                            print("Fertilizer Cost :",fertilizer)
                            print("Labour Cost     :",labour)
                            print("Irrigation Cost :",irrigation)
                            print("\nEstimated Cost  :",total)
                       case 9:
                            seed=5000*acre
                            fertilizer=4000*acre
                            labour=6000*acre
                            irrigation=4000*acre
                            total=seed+fertilizer+labour+irrigation               
                 
                            print("\nCost Report:-\n")
                            print("Crop Name       : Watermelon")
                            print("Land Size       :",acre,"Acres\n")
                            print("Seed Cost       :",seed)
                            print("Fertilizer Cost :",fertilizer)
                            print("Labour Cost     :",labour)
                            print("Irrigation Cost :",irrigation)
                            print("\nEstimated Cost  :",total)
                       case 10:
                            seed=4000*acre
                            fertilizer=3500*acre
                            labour=5000*acre
                            irrigation=3500*acre
                            total=seed+fertilizer+labour+irrigation               
                 
                            print("\nCost Report:-\n")
                            print("Crop Name       : Cucumber")
                            print("Land Size       :",acre,"Acres\n")
                            print("Seed Cost       :",seed)
                            print("Fertilizer Cost :",fertilizer)
                            print("Labour Cost     :",labour)
                            print("Irrigation Cost :",irrigation)
                            print("\nEstimated Cost  :",total)
            case 4:
                 print("\n---Farming Tips---\n")
                 print("1. Wheat")
                 print("2. Rice")
                 print("3. Cotton")
                 print("4. Soyabean")
                 print("5. Maize")
                 print("6. Mustard")
                 print("7. Groundnut")
                 print("8. Bajra")
                 print("9. Watermelon")
                 print("10. Cucumber\n")
                 crop=int(input("Enter your choice: "))
                 match crop:
                       case 1:
                            print("="*40)
                            print("        WHEAT FARMING TIPS")
                            print("="*40)
                            print("• Use certified quality seeds.")
                            print("• Irrigate every 7-10 days.")
                            print("• Remove weeds regularly.")
                            print("• Harvest when grains turn golden.")
                            print("="*40)
                       case 2:
                            print("="*40)
                            print("         RICE FARMING TIPS")
                            print("="*40)
                            print("• Maintain water in the field.")
                            print("• Use healthy seedlings.")
                            print("• Control weeds regularly.")
                            print("• Harvest when grains mature.")
                            print("="*40)
                       case 3:
                            print("="*40)
                            print("        COTTON FARMING TIPS")
                            print("="*40)
                            print("• Grow in black soil.")
                            print("• Avoid waterlogging.")
                            print("• Check for pest attacks.")
                            print("• Pick cotton only after full maturity.")
                            print("="*40)
                       case 4:
                            print("="*40)
                            print("       SOYBEAN FARMING TIPS")
                            print("="*40)
                            print("• Sow before monsoon begins.")
                            print("• Keep proper plant spacing.")
                            print("• Remove weeds in the early stage.")
                            print("• Harvest when pods become dry.")
                            print("="*40)
                       case 5:
                            print("="*40)
                            print("        MAIZE FARMING TIPS")
                            print("="*40)
                            print("• Prepare loose and fertile soil.")
                            print("• Irrigate during flowering.")
                            print("• Apply compost before sowing.")
                            print("• Harvest when cobs are fully mature.")
                            print("="*40)
                       case 6:
                            print("="*40)
                            print("      MUSTARD FARMING TIPS")
                            print("="*40)
                            print("• Sow during the Rabi season.")
                            print("• Avoid excess irrigation.")
                            print("• Remove weeds regularly.")
                            print("• Harvest when pods turn yellow.")
                            print("="*40)
                       case 7:
                            print("="*40)
                            print("     GROUNDNUT FARMING TIPS")
                            print("="*40)
                            print("• Use sandy soil for best growth.")
                            print("• Avoid water stagnation.")
                            print("• Apply gypsum if needed.")
                            print("• Harvest when leaves become yellow.")
                            print("="*40) 
                       case 8:
                            print("="*40)
                            print("       BAJRA FARMING TIPS")
                            print("="*40)
                            print("• Suitable for dry regions.")
                            print("• Needs very little irrigation.")
                            print("• Use organic manure.")
                            print("• Harvest when grains harden.")
                            print("="*40)
                       case 9:
                            print("="*40)
                            print("    WATERMELON FARMING TIPS")
                            print("="*40)
                            print("• Grow in sandy soil.")
                            print("• Water regularly.")
                            print("• Give full sunlight.")
                            print("• Harvest when the fruit sounds hollow.") 
                            print("="*40)
                       case 10:
                            print("="*40)
                            print("     CUCUMBER FARMING TIPS")
                            print("="*40)
                            print("• Water the plants regularly.")
                            print("• Keep the field weed-free.")
                            print("• Harvest fruits every 2-3 days.")
                            print("• Protect plants from insects.")
                            print("="*40)
            case 5:
                 print("\nThank you for using Smart Crop Advisor.")
                 print("Visit Again!\n")
                 break
            case _:
                 print("\nInvalid Choice! Please try again.")