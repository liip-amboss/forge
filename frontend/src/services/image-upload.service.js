import { userApi } from './api';

/**
 * Service to upload a image to a user.
 * @param image File
 * @param id User id
 * @returns HTTP Response
 */
const uploadUserImage = (image, id) => {
  let formData = new FormData();
  formData.append('image', image);

  return userApi.patch(`user/${id}/image/`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};

export { uploadUserImage };
