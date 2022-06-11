/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   file.name()                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By:   qq <qq@student.42lausanne.ch>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/6/11 14:36:41 by      qq            #+#    #+#             */
/*   Updated: 2022/06/10 22:30:51 by      qq          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void ft_comb(int index, int data[], int number);

void ft_print_comb(void)
{
	int	data[3];

	ft_comb(0, data, 0);
}

void ft_comb(int index, int data[], int number)
{
	int  j;
	int	n; 

	if (index == 3)
	{
		j = 0;
		while (j < 3)
		{
			n = data[j] + 48;
			write(1, &n, 1);
			j++;
		}
		if (!(data[0] == 7 && data[1] == 8 && data[2] == 9))
			write(1, ", ", 2);
		return ;
	}
	if (number >= 10)
	{
		return ;
	}
	data[index] = number++;
	ft_comb(index + 1, data, number);
	ft_comb(index + 0, data, number);
}


