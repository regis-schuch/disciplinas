#include "integration_process.h"
#include <stdio.h>

void main() {
    printf("Launcher: MainLauncher\n");

    
    printf("Connecting to Store at https://store.api.com\n");
    
    printf("Connecting to Taxi at https://taxi.api.com\n");
    
    printf("Connecting to Messaging at https://msg.api.com\n");
    

    
    printf("Running Process: PurchaseFlow\n");
    
    step_RetrievePurchase();
    
    step_CheckAndBook();
    
    step_Archive();
    
    
}



void step_RetrievePurchase() {
    printf("[Step] RetrievePurchase\n");
    
    
    printf(" - Read from Store\n");
    
    
}

void step_CheckAndBook() {
    printf("[Step] CheckAndBook\n");
    
    
    printf(" - If purchase >= 150\n");
    
    printf("   * Write to Taxi\n");
    
    printf("   * Write to Messaging\n");
    
    
    
}

void step_Archive() {
    printf("[Step] Archive\n");
    
    
    printf(" - Write to Messaging\n");
    
    
}

