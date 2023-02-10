/*
Purpose: Develop a system to reminde the use of personal medication using Threads.

Input: Medication data only at the time of registration

Output: Reminders of each medicine according to the specified time

Compile: gcc -g -Wall -o Reminder Reminder.c -lpthread
Usage: ./Reminder
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

// Declaração da struct
struct Medication{
    char name[50];
    int wait_Interval;
    int times;
};

// Função que irá controlar o loop individual de um medicamento.
void *Reminder(void* medi){
    struct Medication *med = (struct Medication*) medi;

    time_t t;

    for (int i = 1; i <= med->times; i++){
        time(&t);
        printf("REMINDER: %s %d/%d ## %s", med->name, i, med->times, ctime(&t));
        sleep(med->wait_Interval);
    }
    printf("%s TERMINATED\n", med->name);
    free(med);
    return NULL;
}

// Fuunção main controlando a criação das threads, dos medicamentos e o fim da aplicação
int main(int argc, char* argv[]){
    printf("Task Started!\n");
    printf("=============================================\n");

    // Variável de controle para a quantidade de medicamentos cadastrados pelo usuário
    int total_med;

    printf("Hello! How many medications do you want me to remind you of? ");
    scanf("%d", &total_med);

    // Declaração do array de threads. Como o usuário determina a quantidade de medicamentos, logo, a quantidade de threads tem que ser dinâmica.
    pthread_t thread[total_med];

    // Array de medicamentos
    struct Medication all_med[total_med];
    // Variáveis de apoio para salvar os atributos de cada medicamento do array.
    char d_name[50];
    int w_i;
    int tim;
    
    // Loop responsável por colher e salvar os dados de cada medicamento
    for(int i = 0; i < total_med; i++){
        printf("Drug Name: ");
        scanf("%s", d_name);
        strcpy(all_med[i].name, d_name);

        printf("Interval between doses: ");
        scanf("%d", &w_i);
        all_med[i].wait_Interval = w_i;

        printf("Total of doses: ");
        scanf("%d", &tim);
        all_med[i].times = tim;
    }

    // Loop criador de cada Thread
    for(int i = 0; i < total_med; i++){
        pthread_create(&thread[i], NULL, Reminder, &all_med[i]);
    }

    // Loop finalizador de cada Thread
    for (int i = 0; i < total_med; i++){
        pthread_join(thread[i], NULL);
    }

    printf("TASK TERMINATED :)");
}
// Fim da função MAIN
